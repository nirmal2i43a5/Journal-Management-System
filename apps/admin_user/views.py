from django.shortcuts import render,get_object_or_404,redirect

from apps.user.models import STATUS_ACCEPTED, NormalUser,Article
from apps.reviewer.models import STATUS_ADMIN_PUBLISHED, STATUS_REVIEWER_PUBLISHED, Reviewer
from apps.permissions.models import CustomUser
from django.contrib import messages



def normal_user_index(request):
    users = NormalUser.objects.all()
    context = {
        'title':'Manage User',
        'users':users
    }
    return render(request,'admin/manage_user.html',context)


def reviewer_index(request):
    reviewers = Reviewer.objects.all()
    context = {
        'title':'Manage Reviewer',
        'reviewers':reviewers
    }
    return render(request,'admin/manage_reviewer.html',context)


'''Users list and their articles by Admin '''
def user_view(request):
    users = NormalUser.objects.all()
    
    article_count_list = []
    accepted_articles = []
    articles_published_to_sites = []#articles published to sites  by admin
    
    for user in users:
        user_object = get_object_or_404(CustomUser,id = user.normal_user.id)
        articles = user_object.article_set.all()
        accepted_articles = user_object.article_set.filter(status = STATUS_REVIEWER_PUBLISHED)
        print(accepted_articles,"  accepted articel==============")
        articles_published_to_sites = user_object.article_set.filter(status = STATUS_ADMIN_PUBLISHED)
        print(articles_published_to_sites,"publishded by admin")
        accepted_articles_count = accepted_articles.count()
        articles_published_to_sites_count = articles_published_to_sites.count()
        article_count_list.append({'accepted_articles_count':accepted_articles_count,
                           'articles_published_to_sites_count':articles_published_to_sites_count
                           })
        
    print(accepted_articles_count)
    
    context = {
        'title':'View User',
        'users':zip(users,article_count_list),
        
    }
    return render(request,'admin/articles/user_view.html',context)
    


'''This is the view for viewing published article by reviewer to admin but not by admin to the sites'''
def unpublished_articles(request,user_id):
    unpublished_articles = Article.objects.filter(status = STATUS_REVIEWER_PUBLISHED ,user__pk = user_id)
    user = get_object_or_404(CustomUser, pk = user_id)

    context = {
        'title':'UnPublished Articles',
        'unpublished_articles':unpublished_articles,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'admin/articles/unpublished_articles.html',context)




def article_view(request,article_id):
    article = get_object_or_404(Article, pk = article_id)
    print(article.status)

    context = {
        'title':'Article View',
        'article':article,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'admin/articles/article-view.html',context)



'''Admin Published reviewed articles to sites'''
def publish_articles_to_sites(request,article_id):
    article = Article.objects.get(pk = article_id)
    article.status = STATUS_ADMIN_PUBLISHED
    article.save()
    messages.success(request,"Article Successfully Published")
    return redirect('admin_app:user-view')
    


def published_articles_list(request,user_id):
    published_articles = Article.objects.filter(status = STATUS_ADMIN_PUBLISHED ,user__pk = user_id)
    user = get_object_or_404(CustomUser, pk = user_id)

    context = {
        'title':'Published Articles',
        'published_articles':published_articles,
        
    }
    return render(request,'admin/articles/published_articles.html',context)

