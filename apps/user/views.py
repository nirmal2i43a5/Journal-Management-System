from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib import messages

# Create your views here.

def user_register(request):
    auth_form = CustomUserForm()
    user_form = UserRegisterForm()
    context = {
        'title':'Register',
        'auth_form':auth_form,
        'user_form':user_form
    }
    if request.method == 'POST':
        auth_form = CustomUserForm(request.POST,request.FILES)
        print(auth_form)
        user_form = UserRegisterForm(request.POST,request.FILES)
        print(user_form)
        
        if auth_form.is_valid() and user_form.is_valid():
            
            username = auth_form.cleaned_data["username"]
            password1 = auth_form.cleaned_data["password"]
            password2 = auth_form.cleaned_data["confirm_password"]
            
            if request.FILES.get('image'):
                image_url = request.FILES['image']
            else:
                image_url = None
           
            group = Group.objects.get(name = 'User')
            
            user = CustomUser.objects.create_user(
                username=username, password=password1, confirm_password = password2,
                user_type=group)
        
            user.normaluser.full_name = user_form.cleaned_data['full_name']
            user.normaluser.email = user_form.cleaned_data['email']
            user.normaluser.dob = user_form.cleaned_data['dob']
            user.normaluser.gender = user_form.cleaned_data['gender']
            user.normaluser.contact = user_form.cleaned_data['contact']
            user.normaluser.address = user_form.cleaned_data['address']

            if image_url != None:
                user.normaluser.image = image_url

            user.save()
            user.groups.add(group)#adding user to particular group.ie role
            
                
            messages.success(request, "Successfully Added Parent")
            return redirect('user:register')
        
    return render(request,'users/registers.html',context)
