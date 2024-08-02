from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WildLifeUser

admin.site.register(WildLifeUser, UserAdmin)
