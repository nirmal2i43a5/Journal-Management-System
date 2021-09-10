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
