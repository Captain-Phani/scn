# accounts/urls.py

from django.urls import path
from .views import register, user_profile,login_user

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user-profile'),
    path('login/', login_user, name='token_obtain_pair')
]
