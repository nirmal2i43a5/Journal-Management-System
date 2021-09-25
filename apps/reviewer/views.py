from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import Group
from apps.user.models import NormalUser
from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib import messages
from apps.user.models import Article,Feedback
from apps.user.forms import FeedbackForm
from django.contrib.auth.decorators import login_required, permission_required






@permission_required('reviewer.add_reviewer', raise_exception=True)
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
            messages.success(request, "Successfully Created Reviewer")
            return redirect('admin:reviewer_index')
         
    return render(request,'reviewer/add.html',context)



@permission_required('user.normal_user_view_by_reviewer', raise_exception=True)
def normal_user_index(request):
    users = NormalUser.objects.all()
    total_articles = []
    rejected_articles = []
    accepted_articles = []
    articles_under_review = []
    for user in users:
        user_object = get_object_or_404(CustomUser,id = user.normal_user.id )
        articles = user_object.article_set.all()
        accepted_articles = user_object.article_set.filter(status = STATUS_ACCEPTED)
        rejected_articles = user_object.article_set.filter(status = STATUS_REJECTED)
        article_under_review = user_object.article_set.filter(status = STATUS_UNDER_REVIEW)
        article_publish_to_admin = user_object.article_set.filter(status = STATUS_REVIEWER_PUBLISHED)
        total_articles_count = articles.count()
        accepted_articles_count = accepted_articles.count()
        rejected_articles_count = rejected_articles.count()
        article_under_review_count = article_under_review.count()
        article_publish_to_admin_count = article_publish_to_admin.count()
        
        total_articles.append({'total_articles':total_articles_count,'accepted_articles_count':accepted_articles_count,
                               'rejected_articles_count':rejected_articles_count,'article_under_review_count':article_under_review_count,
                               'article_publish_to_admin':article_publish_to_admin_count})
        
    print(total_articles)
    context = {
        'title':'Manage User',
        'users':zip(users,total_articles)
    }
    
    return render(request,'reviewer/manage_user.html',context)



def view_user_under_review_articles(request,pk):
    articles_under_review = Article.objects.filter(status = STATUS_UNDER_REVIEW,user__pk = pk)
    user = get_object_or_404(CustomUser, pk = pk)

    context = {
        'title':'Articles',
        'articles_under_review':articles_under_review,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'reviewer/articles_under_review.html',context)



def view_user_accepted_articles(request,pk):
    accepted_articles = Article.objects.filter(status = STATUS_ACCEPTED,user__pk = pk)
    user = get_object_or_404(CustomUser, pk = pk)
    # articles = user.article_set.all()
    # checked_articles = []
    # for article in articles:
    #     article_obj = get_object_or_404(Article, pk = article.pk)
    #     article_feedback = article_obj.feedback_set.all()
    #     if article_feedback:
    #         checked_articles.append(article_obj)
            
   
    #
    context = {
        'title':'Accepted Articles',
        'accepted_articles':accepted_articles
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'reviewer/accepted_articles.html',context)


def view_user_rejected_articles(request,pk):
    rejected_articles = Article.objects.filter(status = STATUS_REJECTED,user__pk = pk)
    user = get_object_or_404(CustomUser, pk = pk)
    # articles = user.article_set.all()
    # checked_articles = []
    # for article in articles:
    #     article_obj = get_object_or_404(Article, pk = article.pk)
    #     article_feedback = article_obj.feedback_set.all()
    #     if article_feedback:
    #         checked_articles.append(article_obj)
            
   
    #
    context = {
        'title':'Rejected Articles',
        'rejected_articles':rejected_articles,
        # 'articles_review_feedback':zip(articles_under_review,checked_articles),
        # 'checked_articles':checked_articles,
        
    }
    return render(request,'reviewer/rejected_articles.html',context)



def check_user_article(request,pk):
    article = get_object_or_404(Article, pk = pk)
    context = {
        'title':'Article Check',
        'article':article,
        'form':FeedbackForm()
    }
    return render(request,'reviewer/check-user-article.html',context)



@permission_required('user.add_feedback', raise_exception=True)
def article_feedback(request):
    
    userId = request.POST['userId']
    articleId = request.POST['articleId']
    feedback = request.POST['feedback']
    status = request.POST['status']
    article_object = get_object_or_404(Article,pk = articleId)
    
    if status == 'Accepted':
        article_object.status = STATUS_ACCEPTED 
        article_object.save(update_fields=['status'])
    elif status == 'Rejected':
        article_object.status = STATUS_REJECTED
        article_object.save(update_fields=['status'])     
           
    feedback = Feedback(feedback = feedback, status = status)
    feedback.user = get_object_or_404(CustomUser,pk = userId)
    feedback.article = article_object
    feedback.save()
    
    messages.success(request,"Successfully Review Paper")
    return redirect('reviewer:user-under-review-articles',userId)



@permission_required('user.article_publish_to_admin_by_reviewer', raise_exception=True)
def publish_to_admin(request,user_id,article_id):
    reviewer_object = get_object_or_404(Reviewer, reviewer_user__pk = request.user.id)
    print(reviewer_object.reviewer_user.username)
    article = Article.objects.get(pk = article_id)
    article.reviewed_by = reviewer_object
    article.status = STATUS_REVIEWER_PUBLISHED
    article.save()
    messages.success(request,"Article Successfully Published to Admin")
    return redirect('reviewer:user-accepted-articles',user_id)
    