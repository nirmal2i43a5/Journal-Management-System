from django.urls import path
from .views import *

urlpatterns = [
       path('user_password_reset/', user_set_password, name="set_change_password"),
           path('change_password/', change_password, name="change_password"),
             path('profile_update/', update_admin_profile, name="admin_profile_update"),
              path('reviewer/profile_update/', update_reviewer_profile, name="update_reviewer_profile"),
                path('user/profile_update/', update_user_profile, name="update_user_profile"),
  
]
