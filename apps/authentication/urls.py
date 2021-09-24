from django.urls import path
from .views import *

urlpatterns = [
       path('user_password_reset/', user_set_password, name="set_change_password"),
        path('profile_update/', UpdateAdminProfile, name="admin_profile_update"),
           path('change_password/', change_password, name="change_password"),
  
]
