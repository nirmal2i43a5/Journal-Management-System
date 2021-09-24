"""this views can be access by both student and staff"""

from django.contrib import messages
from django.shortcuts import render, redirect                    
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from student_management_app.django_forms.forms import (
# 	EditCustomUserForm
# )
from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from apps.permissions.models import (CustomUser)



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
			update_session_auth_hash(request, password_reset_form.user)  # Important!

			messages.success(request, "Your Password is Successfully Change")
			return redirect('login')
	context =  {
         'title':'Reset Password',
     			# 'user_role_form': user_role_form,
             'reset_form': password_reset_form}
	return render(request, 'user_reset_password/set_password.html',context)







def change_password(request):
    
	if request.user.is_superuser:#this is not adminuser
		PassForm = PasswordChangeForm(request.user)

		if request.method == 'POST':
    		# i dont see instance when changing password
			PassForm = PasswordChangeForm(user=request.user, data=request.POST)

			if PassForm.is_valid():
				PassForm.save()
				update_session_auth_hash(request, PassForm.user)  # Important!

				messages.success(request, "Your password is successfully updated.Now you can login with your new password.")
				return redirect('login')

		context = {
			'change_form': PassForm
		}
		return render(request, 'user_reset_password/change_password.html', context)




@permission_required('student_management_app.change_adminuser', raise_exception=True)
def UpdateAdminProfile(request):

	if request.user.is_superuser:#this is not adminuser
		custom_form = EditCustomUserForm(instance=request.user)
		admin_form = SystemAdminForm(instance=request.user)
		PassForm = PasswordChangeForm(request.user)

		if request.method == 'POST' and 'admin_submit' in request.POST:
			custom_form = EditCustomUserForm(request.POST, instance=request.user)
			# error with request.user.adminuser
			admin_form = SystemAdminForm(request.POST, request.FILES, instance=request.user)
			print(admin_form)
			if custom_form.is_valid() and admin_form.is_valid():
				custom_form.save()  # call save to forms.py
				admin_form.save()
				messages.success(request, "Your record is successfully updated")
				return redirect('admin_profile_update')


		password_change_form(request)

		context = {
			'custom_form': custom_form,
			'admin_form': admin_form,
			'PassForm': PassForm
		}

		return render(request, 'profile/edit_admin_profile.html', context)



	# if request.user.is_superuser and request.user.adminuser:	
	# 	print("-------I am here2")
	# 	custom_form = EditCustomUserForm(instance=request.user)
	# 	admin_form = SystemAdminForm(instance=request.user.adminuser)
	# 	PassForm = PasswordChangeForm(request.user)

	# 	if request.method == 'POST' and 'admin_submit' in request.POST:
	# 		custom_form = EditCustomUserForm(request.POST, instance=request.user)
	# 		# error with request.user.adminuser
	# 		admin_form = SystemAdminForm(request.POST, request.FILES, instance=request.user.adminuser)
	# 		if custom_form.is_valid() and admin_form.is_valid():
	# 			custom_form.save()  # call save to forms.py
	# 			admin_form.save()
	# 			messages.success(request, "Your record is successfully updated")
	# 			return redirect('login')

	# 	password_change_form(request)

	# 	context = {
	# 		'custom_form': custom_form,
	# 		'admin_form': admin_form,
	# 		'PassForm': PassForm
	# 	}

	# 	return render(request, 'profile/edit_admin_profile.html', context)
