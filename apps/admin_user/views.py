from django.shortcuts import render
from apps.user.models import NormalUser
from apps.reviewer.models import Reviewer



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


def user_view(request):
    users = NormalUser.objects.all()
    context = {
        'title':'View User',
        'users':users
    }
    return render(request,'admin/articles/user_view.html',context)
    

def view_reviewed_articles(request,pk):
    articles_under_review = Article.objects.filter(status = STATUS_UNDER_REVIEW,user__pk = pk)
    user = get_object_or_404(CustomUser, pk = pk)

    context = {
        'title':'Articles',
        'articles_under_review':articles_under_review,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'reviewer/articles_under_review.html',context)