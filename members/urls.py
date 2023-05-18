from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('close-session/', views.deslogin, name='logout'),
    path('show/profile/<int:pk>/', views.profile, name='profile'),
    
]