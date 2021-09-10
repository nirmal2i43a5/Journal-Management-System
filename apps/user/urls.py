from apps.user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('register/',user_register,name='register'),
        path('upload-article/',upload_article,name='upload-article'),
        path('article-view/<pk>/',article_view,name='article-view'),
    path('article-list/', article_list, name='article-list'),
    
]
