from apps.user.views import *
from django.urls import path



urlpatterns = [
    path('register/',user_register,name='register'),
     path('login/',user_login,name='login'),
    
]
