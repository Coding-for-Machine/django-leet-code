from django.urls import path
from .views import LoginPage, ProfilePage, RegisterPage, LogoutPage



urlpatterns = [
    path('', ProfilePage, name='profile'),
    path('login/', LoginPage, name='login'),
    path('register/', RegisterPage, name='register'),
    path('logout/', LogoutPage, name='lpgout'),
]
