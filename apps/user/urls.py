from apps.user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('register/',user_register,name='register'),
        path('upload-journal/',upload_journal,name='upload-journal'),
    # path('/article-list', user_article_list, name='user-article-list'),
    
]
