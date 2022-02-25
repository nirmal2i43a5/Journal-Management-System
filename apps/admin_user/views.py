import datetime
from apps.admin_user.models import Category,Notice
from django.shortcuts import render,get_object_or_404,redirect
from apps.user.models import STATUS_ACCEPTED, NormalUser,Article
from apps.reviewer.models import STATUS_ADMIN_PUBLISHED, STATUS_REVIEWER_PUBLISHED, Reviewer
from apps.permissions.models import CustomUser
from .forms import ArticleCategoryForm,NoticeForm
from django.contrib import messages
from django.contrib.auth.decorators import  permission_required



@permission_required('admin_user.add_category', raise_exception=True)
def add_category(request):
    form = ArticleCategoryForm()
    if request.method == 'POST':
        form = ArticleCategoryForm(request.POST,request.FILES)
        form.save()
        messages.success(request, "Successfully Added Category.")
        return redirect('admin_app:add_category')
    
    context = {
        'form':form
    }
    return render(request,'admin/category/add.html',context)



@permission_required('admin_user.change_category', raise_exception=True)
def edit_category(request,pk):
    instance = get_object_or_404(Category, pk = pk)
    form = ArticleCategoryForm(instance = instance)
    if request.method == 'POST':
        form = ArticleCategoryForm(request.POST,request.FILES, instance = instance)
        form.save()
        messages.success(request, "Successfully Edited Category.")
        return redirect('admin_app:category_index')
    
    context = {
        'form':form,
        'instance':instance
    }
    return render(request,'admin/category/add.html',context)


@permission_required('admin_user.delete_category', raise_exception=True)
def delete_category(request,pk):
    instance = get_object_or_404(Category, pk = pk)
    instance.delete()
    messages.success(request, "Successfully Deleted Category.")
    return redirect('admin_app:category_index')
    

@permission_required('admin_user.view_category', raise_exception=True)
def category_index(request):
    categories = Category.objects.all()
    context = {
        'title':'Manage Category',
        'categories':categories
    }
    return render(request,'admin/category/index.html',context)



@permission_required('user.view_normaluser', raise_exception=True)
def normal_user_index(request):
    users = NormalUser.objects.all()
    context = {
        'title':'Manage User',
        'users':users
    }
    return render(request,'admin/manage_user.html',context)



@permission_required('reviewer.view_reviewer', raise_exception=True)
def reviewer_index(request):
    reviewers = Reviewer.objects.all()
    context = {
        'title':'Manage Reviewer',
        'reviewers':reviewers
    }
    return render(request,'admin/manage_reviewer.html',context)



'''Users list and their articles by Admin '''
@permission_required('user.view_normaluser', raise_exception=True)
def user_view(request):
    
    users = NormalUser.objects.all()
    
    article_count_list = []
    accepted_articles = []
    articles_published_to_sites = []#articles published to sites  by admin
    
    for user in users:
        user_object = get_object_or_404(CustomUser,id = user.normal_user.id)
        articles = user_object.article_set.all()
        accepted_articles = user_object.article_set.filter(status = STATUS_REVIEWER_PUBLISHED)
        articles_published_to_sites = user_object.article_set.filter(status = STATUS_ADMIN_PUBLISHED)
        accepted_articles_count = accepted_articles.count()
        articles_published_to_sites_count = articles_published_to_sites.count()
        article_count_list.append(
                            {'accepted_articles_count':accepted_articles_count,
                           'articles_published_to_sites_count':articles_published_to_sites_count
                           })
            
    context = {
        'title':'Manage Users Article',
        'users':zip(users,article_count_list),
        
    }
    
    return render(request,'admin/articles/user_view.html',context)
    


'''This is the view for viewing published article by reviewer to admin but not by admin to the sites'''
@permission_required('user.view_unpublish_articles', raise_exception=True)
def unpublished_articles(request,user_id):
    unpublished_articles = Article.objects.filter(status = STATUS_REVIEWER_PUBLISHED ,user__pk = user_id)
    user = get_object_or_404(CustomUser, pk = user_id)

    context = {
        'title':'UnPublished Articles',
        'unpublished_articles':unpublished_articles,
        
    }
    return render(request,'admin/articles/unpublished_articles.html',context)



@permission_required('user.each_article_view', raise_exception=True)
def article_view(request,article_id):
    article = get_object_or_404(Article, pk = article_id)
    print(article.status)

    context = {
        'title':'Article View',
        'article':article,
        
    }
    return render(request,'admin/articles/article-view.html',context)

           

'''Admin Published reviewed articles to sites'''
@permission_required('user.publish_articles_to_sites', raise_exception=True)
def publish_articles_to_sites(request,article_id):
    article = Article.objects.get(pk = article_id)
    article.status = STATUS_ADMIN_PUBLISHED
    # article.updated_at = datetime.date.today()
    article.save()
    messages.success(request,"Article Successfully Published")
    return redirect('admin_app:user-view')
    
    

@permission_required('user.view_publish_articles_to_sites', raise_exception=True)
def published_articles_list(request,user_id):
    published_articles = Article.objects.filter(status = STATUS_ADMIN_PUBLISHED ,user__pk = user_id)
    user = get_object_or_404(CustomUser, pk = user_id)

    context = {
        'title':'Published Articles',
        'published_articles':published_articles,
        
    }
    return render(request,'admin/articles/published_articles.html',context)



@permission_required('admin_user.add_notice', raise_exception=True)
def add_notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        try:     
            if form.is_valid():
                instance = form.save(commit = False)
                
                try:
                    #if one notice is already active then it will become inactive if i add new one
                    notice_item = get_object_or_404(Notice, status=True)
                    notice_item.status=False
                    notice_item.save()
                except:
                    instance.save()
                instance.save()
                title = form.cleaned_data['title']
                user=request.user
                
                messages.success(request, "Notice is Added Successfully.")
                return redirect('admin_app:notice-index')
        except:
            messages.error(request, "Failed to Add Notice.")
            return redirect('admin_app:notice-add')
    else:
        form = NoticeForm()
   
    context = {'form':form,'title':'Notice'}
    return render(request, "admin/notices/add_notice.html", context)


@permission_required('admin_user.change_notice', raise_exception=True)
def edit_notice(request, notice_id):
    notice_instance = get_object_or_404(Notice, id = notice_id)
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES, instance = notice_instance)
   
        try:     
            if form.is_valid():
                form.save()
                messages.success(request, "Notice is Updated Successfully.")
                return redirect('admin_app:notice-index')
        except:
            messages.error(request, "Failed to Updated Notice.")
            return redirect('admin_app:notice-edit')
            
    else:
        form = NoticeForm(instance = notice_instance)
   
    context = {'form':form,'title':'Notice','notice_instance':notice_instance}
    return render(request, "admin/notices/add_notice.html", context)


@permission_required('amin_user.delete_notice', raise_exception=True)
def delete_notice(request, notice_id):
    try:
        notice = get_object_or_404(Notice, id = notice_id)
        notice.delete()
        messages.success(request, f' Notice is Deleted Successfully')
        return redirect('admin_app:notice-index')
    except:
        messages.error(request, 'Failed To index Notice')
        return redirect('admin_app:notice-delete')


# @permission_required('announcement.view_notice', raise_exception=True)
def manage_notice(request):
    notices = Notice.objects.all()
    context = {'notices': notices,'title':'Manage Notice'}
    return render(request, 'admin/notices/manage_notice.html', context)



def update_notice_status(request):
    if request.is_ajax():    
        id=request.GET.get('id')
        st=get_object_or_404(Notice,pk=id)
        if st.status == False:
            st.status=True
            # notice = get_object_or_404(Notice, status=True)
            # notice.status=False#make previous inactive
            # notice.save()
            st.save()
        else:
            st.status=False
            st.save()
            
        notice_data = Notice.objects.all()
        
    '''Due to   design fluctuation, I am rendering to notice_list.html'''
    return render(request, 'admin/notices/notice_list.html', {'notices':notice_data})







