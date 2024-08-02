from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from .views import CustomLogoutView

app_name = "core"
urlpatterns = [
    path('home/', views.home_redirect, name='home'),  # Root URL maps to home view
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact_form, name='contact_form'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('about/', views.about, name="about"),
    path('parks/', views.parks, name='parks'),
    path('booking/', views.booking, name='booking'),
    path('community/' , views.community, name='community'),
    path('forum/', views.forum, name = "forum"),
    path('donate/', views.donate, name= "donate"),
    path('donation/', views.donation, name='donation'),
    path('events/', views.events, name='events'),
    path('upload_report', views.upload_report, name='upload_report'),
    path('view_reports', views.view_reports, name='view_reports'),
    path('booking/', views.booking_park, name='booking_park'),
    path('booking_form/', views.booking_form, name='booking_form'),

    
   

    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
