from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Report model to store uploaded files and associated metadata
class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Custom user model extending AbstractUser to include user type
class WildLifeUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('researcher', 'Researcher'),
        ('tourist', 'Tourist'),
    ]
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

    # Override the related names to avoid conflicts with AbstractUser
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='wildlife_user_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='wildlife_user_permissions', 
        blank=True
    )
    
    def __str__(self):
        return self.username
