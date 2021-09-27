"""this views can be access by both student and staff"""

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from student_management_app.django_forms.forms import (
# 	EditCustomUserForm
from django.views import View
from .forms import EditCustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from apps.reviewer.forms import ReviewerRegisterForm
from apps.user.forms import UserRegisterForm


@login_required
def user_set_password(request):
    # user_role_form = UserRoleForm()
    # username = request.GET.get('user')
    password_reset_form = SetPasswordForm(request.user)

    if request.method == 'POST':
        # i dont see instance when changing password
        # username = request.POST['user']
        password_reset_form = SetPasswordForm(request.user, data=request.POST)

        if password_reset_form.is_valid():
            password_reset_form.save()
            update_session_auth_hash(
                request, password_reset_form.user)  # Important!

            messages.success(request, "Your Password is Successfully Change")
            return redirect('login')
    context = {
        'title': 'Reset Password',
        # 'user_role_form': user_role_form,
        'reset_form': password_reset_form}
    return render(request, 'user_reset_password/set_password.html', context)


def change_password(request):
    if request.user.is_superuser:  # this is not adminuser
        PassForm = PasswordChangeForm(request.user)

        if request.method == 'POST':
            # i dont see instance when changing password
            PassForm = PasswordChangeForm(user=request.user, data=request.POST)

            if PassForm.is_valid():
                PassForm.save()
                update_session_auth_hash(request, PassForm.user)  # Important!

                messages.success(
                    request, "Your password is successfully updated.Now you can login with your new password.")
                return redirect('login')

        context = {
            'change_form': PassForm
        }
        return render(request, 'user_reset_password/change_password.html', context)


def password_change_form(request):
    if request.method == 'POST' and 'change_pass_button' in request.POST:
        # i dont see instance when changing password
        PassForm = PasswordChangeForm(user=request.user, data=request.POST)

        if PassForm.is_valid():
            PassForm.save()
            update_session_auth_hash(request, PassForm.user)  # Important!

            messages.success(
                request, "Your password is successfully updated.Now you can login with your new password.")
            return redirect('login')


def update_admin_profile(request):
    if request.user.is_superuser:
        custom_form = EditCustomUserForm(instance=request.user)
        # admin_form = SystemAdminForm(instance=request.user)
        PassForm = PasswordChangeForm(request.user)

        if request.method == 'POST' and 'admin_update' in request.POST:
            custom_form = EditCustomUserForm(
                request.POST, instance=request.user)
            if custom_form.is_valid():
                custom_form.save()
                messages.success(
                    request, "Your record is successfully updated")
                return redirect('admin_profile_update')

        password_change_form(request)

        context = {
               'title':'Profile Update',
            'custom_form': custom_form,
            'PassForm': PassForm
        }

        return render(request, 'profile/edit_admin_profile.html', context)



def update_reviewer_profile(request):
    
	custom_form = EditCustomUserForm(instance=request.user)
	reviewer_form = ReviewerRegisterForm(instance=request.user.reviewer)
	PassForm = PasswordChangeForm(request.user)

	if request.method == 'POST' and 'reviewer_update' in request.POST:
		custom_form = EditCustomUserForm(request.POST, instance=request.user)
		reviewer_form = ReviewerRegisterForm(request.POST, request.FILES, instance=request.user.reviewer)
  
		if custom_form.is_valid() and reviewer_form.is_valid():
			custom_form.save()
			reviewer_form.save()
			messages.success(
				request, "Your record is successfully updated")
			return redirect('update_reviewer_profile')

	password_change_form(request)

	context = {
        'title':'Profile Update',
		'customuser_form': custom_form,
		'reviewer_form': reviewer_form,
		'PassForm': PassForm
	}

	return render(request, 'profile/edit_reviewer_profile.html', context)



def update_user_profile(request):
    
	custom_form = EditCustomUserForm(instance=request.user)
	user_form = UserRegisterForm(instance=request.user.normaluser)
	PassForm = PasswordChangeForm(request.user)

	if request.method == 'POST' and 'user_update' in request.POST:
		custom_form = EditCustomUserForm(request.POST, instance=request.user)
		user_form = UserRegisterForm(request.POST, request.FILES, instance=request.user.normaluser)
  
		if custom_form.is_valid() and user_form.is_valid():
			custom_form.save()
			user_form.save()
			messages.success(
				request, "Your record is successfully updated")
			return redirect('update_user_profile')

	password_change_form(request)

	context = {
     'title':'Profile Update',
		'customuser_form': custom_form,
		'user_form': user_form,
		'PassForm': PassForm
	}

	return render(request, 'profile/edit_user_profile.html', context)
