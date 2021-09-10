from apps.user.views import *
from apps.reviewer.views import *
from django.urls import path

app_name = 'reviewer'

urlpatterns = [
    path('add/',add_reviewer,name='add'),
        path('upload-article/',upload_article,name='upload-article'),
        path('article-view/<pk>/',article_view,name='article-view'),
    path('article-list/', article_list, name='article-list'),
    
]
