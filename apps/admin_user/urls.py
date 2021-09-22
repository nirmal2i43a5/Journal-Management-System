
from apps.admin_user.views import *
from django.urls import path

app_name = 'admin_app'

urlpatterns = [
    path('user/index/',normal_user_index,name='normal-user-index'),
    path('reviewer/index/',reviewer_index,name='reviewer-index'),
    path('user-view/',user_view,name='user-view'),
    
    
    
]

