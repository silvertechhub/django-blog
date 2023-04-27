from django.urls import path
from django.contrib.auth import views as authviews

from .views import register
from .forms import LoginForm

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', authviews.LoginView.as_view(template_name='registartion/login.html', authentication_form=LoginForm), name='login'),
    
]