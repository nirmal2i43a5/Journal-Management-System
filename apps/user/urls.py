from apps.user.views import user_register
from django.urls import path

app_name = 'user'


urlpatterns = [
    path('register/',user_register,name='register')
]
