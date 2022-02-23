from apps.user.views import *
from apps.reviewer.views import *
from django.urls import path

app_name = 'reviewer'

urlpatterns = [
    path('add/', add_reviewer, name='add_reviewer'),
    path('edit/<pk>/', edit_reviewer, name='edit_reviewer'),
    path('delete/<pk>/', delete_reviewer, name='delete_reviewer'),
    path('upload-article/', upload_article, name='upload-article'),
    path('article-view/<pk>/', article_view, name='article-view'),
    path('user/index/', normal_user_index, name='normal-user-index'),
    path('user-under-review-articles/<pk>/',
         view_user_under_review_articles, name='user-under-review-articles'),
    path('user-accepted/<pk>/', view_user_accepted_articles,
         name='user-accepted-articles'),
    path('user-rejected/<pk>/', view_user_rejected_articles,
         name='user-rejected-articles'),
    path('check-article/<pk>/', check_user_article, name='check_user_article'),
    path('feedback/', article_feedback, name='article_feedback'),
    path('publish_to_admin/<user_id>/<article_id>/',
         publish_to_admin, name='publish_to_admin'),

]
