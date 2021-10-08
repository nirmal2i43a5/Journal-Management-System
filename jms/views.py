
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from apps.user.models import STATUS_ADMIN_PUBLISHED, NormalUser,Article
from apps.admin_user.models import Category
from apps.reviewer.models import STATUS_ACCEPTED, STATUS_REJECTED, STATUS_REVIEWER_PUBLISHED, STATUS_UNDER_REVIEW, Reviewer
from datetime import datetime, timedelta, time
from apps.user.filters import ArticleFilter


def first_page(request):
    categories = Category.objects.all()
    published_articles = Article.objects.filter(status = STATUS_ADMIN_PUBLISHED).order_by('-updated_at')
    filter_form = ArticleFilter()
    title = request.GET.get('title')
    category = request.GET.get('category')
    
    if title or category:
        filter_articles = ArticleFilter(request.GET, queryset=published_articles).qs
        context = {
        'title':'Journal Management System',
        'category':Category.objects.all(),
        'published_articles':filter_articles,
        'filter_form':filter_form
        
    }
        return render(request,'home.html',context)
        
   
    # article_list = ArticleFilter(request.GET, queryset=published_articles)
    context = {
        'title':'Journal Management System',
        'category':categories,
        'published_articles':published_articles,
        'filter_form':filter_form
        
    }
    return render(request,'home.html',context)


def dashboard(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    
    users = NormalUser.objects.all()
    reviewers = Reviewer.objects.all()
    unpublish_articles_by_admin = Article.objects.filter(status = STATUS_REVIEWER_PUBLISHED)

    '''I am using datetimefield instead of datefield so filter in this way'''
    today_publish_by_admin = Article.objects.filter(status = STATUS_ADMIN_PUBLISHED,updated_at__gte = today_start).filter(updated_at__lte = today_end)
    
    
    # --------For normal user dashboard
    total_user_articles_submitted = Article.objects.filter(user = request.user)
    total_user_article_accepted = Article.objects.filter(user = request.user,status = STATUS_ADMIN_PUBLISHED)
    total_user_article_rejected = Article.objects.filter(user = request.user,status = STATUS_REJECTED)
    total_user_article_under_review = Article.objects.filter(user = request.user,status = STATUS_UNDER_REVIEW)
    
    # ----------------------for reviewer dashboard
    today_accepted_article_by_reviewer = Article.objects.filter(status = STATUS_ACCEPTED,updated_at__gte = today_start).filter(updated_at__lte = today_end)
    today_rejected_article_by_reviewer  = Article.objects.filter(status = STATUS_REJECTED,updated_at__gte = today_start).filter(updated_at__lte = today_end)
    today_publish_article_to_admin = Article.objects.filter(status = STATUS_REVIEWER_PUBLISHED,updated_at__gte = today_start).filter(updated_at__lte = today_end)
    article_under_review = Article.objects.filter(status = STATUS_UNDER_REVIEW)
    total_publish_to_admin = Article.objects.filter(status = STATUS_REVIEWER_PUBLISHED)
    

    context = {
        'title': 'Dashboard',
        'normaluser_count':users.count(),
        'reviewer_count':reviewers.count(),
        'unpublish_count':unpublish_articles_by_admin.count(),
        'today_publish_count':today_publish_by_admin.count(),
        'total_user_articles_submitted_count':total_user_articles_submitted.count(),
        'total_user_article_accepted_count':total_user_article_accepted.count(),
        'total_user_article_rejected_count':total_user_article_rejected.count(),
        'total_user_article_under_review_count':total_user_article_under_review.count(),
        'today_accepted_article_by_reviewer_count':today_accepted_article_by_reviewer.count(),
        'today_rejected_article_by_reviewer_count':today_rejected_article_by_reviewer.count(),
        'today_publish_article_to_admin_count':today_publish_article_to_admin.count(),
        'article_under_review_count':article_under_review.count(),
        'total_publish_to_admin_count':total_publish_to_admin.count()
        
        
        
        
        
    }
    return render(request, 'dashboard.html', context)


def user_login(request):

    form = LoginForm()

    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group or request.user.is_superuser:
                return redirect('home')
            else:
                messages.error(request, "Invalid User")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Details")
            return redirect('login')

    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('login')
