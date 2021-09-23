
from apps.admin_user.views import *
from django.urls import path

app_name = 'admin_app'

urlpatterns = [
    path('user/index/',normal_user_index,name='normal-user-index'),
    path('reviewer/index/',reviewer_index,name='reviewer-index'),
    path('user-view/',user_view,name='user-view'),
      path('article_view/<article_id>/',article_view,name='article_view'),
    path('unpublished-articles/<user_id>/',unpublished_articles,name='unpublished-articles'),
    path('publish_articles_to_sites/<article_id>/',publish_articles_to_sites,name='publish_articles_to_sites'),
    path('published-articles/<user_id>/',published_articles_list,name='published-articles'),
    
    
    
]

