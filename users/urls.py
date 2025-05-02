from django.urls import path
from .views import (
    profile_view, edit_profile_view, profile_settings_view, profile_change_email, profile_verify_email,
    profile_delete_view
)

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit/', edit_profile_view, name='edit_profile'),
    path('onboarding/', edit_profile_view, name='onboarding_profile'),
    path('settings/', profile_settings_view, name='profile_settings'),
    path('profile_change_email/', profile_change_email, name='profile_change_email'),
    path('profile_verify_email/', profile_verify_email, name='profile_verify_email'),
    path('profile_delete/', profile_delete_view, name='profile_delete'),
    path('@<str:username>/', profile_view, name='user_profile'),
]
