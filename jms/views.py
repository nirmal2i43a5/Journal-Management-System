
import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from apps.user.models import STATUS_ADMIN_PUBLISHED, NormalUser,Article
from apps.reviewer.models import STATUS_REVIEWER_PUBLISHED, Reviewer
from datetime import datetime, timedelta, time



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
    
    context = {
        'title': 'Dashboard',
        'normaluser_count':users.count(),
        'reviewer_count':reviewers.count(),
        'unpublish_count':unpublish_articles_by_admin.count(),
        'today_publish_count':today_publish_by_admin.count()
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
