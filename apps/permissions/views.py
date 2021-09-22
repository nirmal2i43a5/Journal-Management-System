from django.shortcuts import render, redirect,get_object_or_404
from .forms import RoleForm, PermissionForm, UserPermissionSearch,ShowRolePermission
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required  
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin # new
)
from django.contrib.auth.decorators import login_required, permission_required  


class UserRoleCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Group
    template_name = "roles/add_role.html"
    form_class = RoleForm
    permission_required = 'auth.add_group'
    success_message = 'Role is Added Successfully'

    def get_success_url(self, **kwargs):
        return reverse_lazy('role_app:add_role')

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.save()
        return super(UserRoleCreate, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Role'
        return context
    
    
class UserRoleUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Group
    template_name = "roles/add_role.html"
    form_class = RoleForm
    permission_required = 'auth.change_group'
    context_object_name = 'role'  # default context_object_name is object
    success_message = 'Role is Updated Successfully'

    def get_success_url(self, **kwargs):
        return reverse_lazy('role_app:edit_role', kwargs={'pk': self.object.pk})

    # form will automatically come from form_class when post request hit
    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.save()
        return super(UserRoleUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Role'
        return context

class UserRoleMange(PermissionRequiredMixin, SuccessMessageMixin, ListView):
    model = Group
    template_name = "roles/manage_role.html"
    context_object_name = 'roles'
    permission_required = 'view.add_group'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Manage Role'
        return context


class UserPermissionCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = Permission
    template_name = "permissions/add_permission.html"
    form_class = PermissionForm
    permission_required = 'auth.add_permission'
    success_message = 'Permission is Added Successfully'

    def get_success_url(self, **kwargs):
        return reverse_lazy('role_app:add_permission')

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.save()
        return super(UserPermissionCreate, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Permission'
        return context


# class UserPermissionMange(SuccessMessageMixin, ListView):
# 	model = Permission
# 	template_name = "permissions/add_permission.html"
# 	context_object_name = 'permissons'

# def UserPermissionMange(request):
#     form = UserPermissionSearch()
#     role = request.POST.get('role')#gives role id
#     group = Group.objects.get(name  = 'Parent')
#     # # user.get_group_permissions()#permisssion related to user
#     if role:
#         # permissions = roles.permissions.all()#i can also retrieve with this when role does not gives id
        # permissions = Permission.objects.filter(group__id = role)#i receive id from role.so i use implement this logic
#         form = UserPermissionSearch(initial={'role':role})#this show instance in form even after post search form 
#         context = {'permissions': permissions, 'form': form,'role':role}
#         return render(request, 'permissions/manage_permission.html', context)
    
#     if request.method == 'POST':
#         permission_id = request.POST.getlist('permission')
#         group.permissions.add(permission_id)
#         print(permission_id)
        
#     context = {'form': form,'role':role}
#     return render(request, 'permissions/manage_permission.html', context)



# Search for role permission 
@permission_required('auth.view_permission', raise_exception=True)
def user_permission_manage(request):
    form = UserPermissionSearch()  
    role = request.POST.get('role')#gives role id from search permission
    
    if role:
        group = get_object_or_404(Group,id = role)
        permission_instance_form = ShowRolePermission(instance = group)#showing permission form instance 
        form = UserPermissionSearch(initial={'role':role})#this show instance in form even after post search form 
        
        context = {
            'title':'Manage Permission',
                # 'role_form_search': form,
                'role':role,
                'role_object':get_object_or_404(Group, id = role),
                'permission_instance_form':permission_instance_form,
                }
        return render(request, 'permissions/manage_permission.html', context)
       
    context = {'role_form_search': form,
               'role':role,
               'title':'Manage Permission'}
    return render(request, 'permissions/manage_permission.html', context)



# Updating permission 

def save_permission(request):
    
    if request.method == 'POST' and 'role_id' in request.POST:
        
        role = request.POST.get('role_id')
        group = get_object_or_404(Group,id = role)
        
        permission_instance_form = ShowRolePermission(instance = group, data = request.POST)#showing permission form instance 
        if permission_instance_form.is_valid():
            
            permission_instance_form.save()
            messages.success(request,"Permission is Successfully Modified ")
            
            # return redirect('role_app:manage_permission')
            context = {
                # 'role_form_search': UserPermissionSearch(initial={'role':role}),#also show role instance in search form when u redirect in the same page
                'role':role,
                'permission_instance_form':permission_instance_form,#this is form which shows all permissions after I filer role
                 }
            return render(request, 'permissions/manage_permission.html', context)
        else:
            return HttpResponse("<h1>Something went wrong!</h1>")
           
        
 

