from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import Group
from apps.user.models import NormalUser
from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib import messages
from apps.user.models import Article,Feedback






def add_reviewer(request):
    auth_form = CustomUserForm()
    reviewer_user = ReviewerRegisterForm()
    context = {
        'title':'Register',
        'auth_form':auth_form,
        'reviewer_user':reviewer_user
    }
    if request.method == 'POST':
        auth_form = CustomUserForm(request.POST,request.FILES)
        reviewer_user = ReviewerRegisterForm(request.POST,request.FILES)
        
        if auth_form.is_valid() and reviewer_user.is_valid():
            
            username = auth_form.cleaned_data["username"]
            
            if request.FILES.get('image'):
                image_url = request.FILES['image']
            else:
                image_url = None
           
            group = Group.objects.get(name = 'Reviewer')
            
            
            user = CustomUser.objects.create_user(
                username=username, password="password",
                user_type=group)
        
    
            user.reviewer.full_name = reviewer_user.cleaned_data['full_name']
            user.reviewer.email = reviewer_user.cleaned_data['email']
            user.reviewer.dob = reviewer_user.cleaned_data['dob']
            user.reviewer.gender = reviewer_user.cleaned_data['gender']
            user.reviewer.contact = reviewer_user.cleaned_data['contact']
            user.reviewer.address = reviewer_user.cleaned_data['address']

            if image_url != None:
                user.reviewer.image = image_url

            user.save()
            user.groups.add(group)#adding user to particular group.ie role
            print(user,"-----group----")
            
                
            messages.success(request, "Successfully Created Reviewer")
            return redirect('admin:reviewer_index')
         
        
    return render(request,'reviewer/add.html',context)



def normal_user_index(request):
    users = NormalUser.objects.all()
    context = {
        'title':'Manage User',
        'users':users
    }
    return render(request,'reviewer/manage_user.html',context)


def view_user_articles(request,pk):
    articles_under_review = Article.objects.filter(status = STATUS_UNDER_REVIEW,user__pk = pk)
    user = get_object_or_404(CustomUser, pk = pk)
    articles = user.article_set.all()
    checked_articles = []
    for article in articles:
        article_obj = get_object_or_404(Article, pk = article.pk)
        article_feedback = article_obj.feedback_set.all()
        if article_feedback:
            checked_articles.append(article_obj)
    # rejected_articles
    # accepted_articles
    #
    print(checked_articles)
    context = {
        'title':'Articles',
        'articles_under_review':articles_under_review,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'reviewer/article-view.html',context)



def check_user_article(request,pk):
    article = get_object_or_404(Article, pk = pk)
    context = {
        'title':'Article Check',
        'article':article
    }
    return render(request,'reviewer/check-user-article.html',context)



def article_feedback(request):
    userId = request.POST['userId']
    articleId = request.POST['articleId']
    feedback = request.POST['feedback']
    print(userId, articleId, feedback)
    feedback = Feedback(feedback = feedback)
    feedback.user = get_object_or_404(CustomUser,pk = userId)
    feedback.article = get_object_or_404(Article,pk = articleId)
    # feedback.status = True
    feedback.save()
    messages.success(request,"Successfully Review Paper")
    return redirect('reviewer:view_user_articles',userId)