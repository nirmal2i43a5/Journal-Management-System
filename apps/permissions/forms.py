from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _

MODELS_TO_HIDE_STD_PERMISSIONS = (
    # ('app_name','mymodel')
    ("auth", "group"),
    ("contenttypes", "content type"),
    ("admin", "log entry"),
)

#remove unnecessary default permission 
def _get_corrected_permissions():
    perms = Permission.objects.all()
    for app_name, model_name in MODELS_TO_HIDE_STD_PERMISSIONS:
        perms = perms.exclude(content_type__app_label=app_name)
        # perms = perms.exclude(content_type__app_label=app_name, codename='change_%s' % model_name)
        # perms = perms.exclude(content_type__app_label=app_name, codename='delete_%s' % model_name)
    return perms

class PermissionField(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        _get_corrected_permissions(), #remove unnecessary default permission 
        widget=FilteredSelectMultiple(_('permissions'), False))


    
class RoleForm(PermissionField):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Respective Role Name'}))
    class Meta:
        model = Group
        fields = '__all__'
        # widgets = {
        #     'permissions': FilteredSelectMultiple("Permission", False, attrs={'rows':'2'}),
        # }

class RoleEditForm(PermissionField):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Respective Role Name','readonly':'readonly'}))
    class Meta:
        model = Group
        fields = '__all__'
        # widgets = {
        #     'permissions': FilteredSelectMultiple("Permission", False, attrs={'rows':'2'}),
        # }

class PermissionForm(PermissionField):
    class Meta:
        model = Permission
        fields = '__all__'
        exclude = ('codename',)
      

        
class UserPermissionSearch(forms.Form):
    role = forms.ModelChoiceField(label = '',empty_label = 'Select User Role',
                                  queryset = Group.objects.all(),
                                  widget=forms.Select(attrs = {'class':'form-control ml-2 mt-1'})
                                  )
    
    
    
#This is the form that is populated when i search permision for respective user in manage_permission--- we edit permission for particular group 
class ShowRolePermission(PermissionField):
    class Meta:
        model = Group
        fields = '__all__'
        exclude = ('name',)
   
   

    
    # class Media:
    #     css = {'all':('/admin/css/widgets.css', 'admin/css/overrides.css'),}
    #     js = ('/admin/jquery.js','/admin/jsi18n/')

