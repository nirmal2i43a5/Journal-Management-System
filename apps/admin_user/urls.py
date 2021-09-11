
from apps.admin_user.views import *
from django.urls import path


urlpatterns = [
    path('user/index/',normal_user_index,name='normal-user-index'),
    path('reviewer/index/',reviewer_index,name='reviewer-index'),
    
    
]

