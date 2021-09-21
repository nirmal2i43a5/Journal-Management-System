from apps.user.views import *
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('register/',user_register,name='register'),
    path('upload-article/',upload_article,name='upload-article'),
    path('article-view/<pk>/',article_view,name='article-view'),
    path('article-under-review/', article_under_review, name='article-under-review'),
    path('article-accepted/', accepted_article_list, name='article-accepted'),
    path('article-rejected/', rejected_article_list, name='article-rejected'),
]



