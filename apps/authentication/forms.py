from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from apps.permissions.models import CustomUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

# class UserRoleForm(forms.ModelForm):

#     role = forms.ModelChoiceField(
#         empty_label="Select roles ", queryset=Group.objects.all())

#     class Meta:
#         model = UserRole
#         fields = '__all__'





