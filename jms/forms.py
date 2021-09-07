from django import forms
from django.utils.translation import gettext_lazy as _
from apps.permissions.models import CustomUser
from apps.permissions.models import *

class LoginForm(forms.ModelForm):
     
    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": " Enter Username", }))
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(
        attrs={"placeholder": " Enter Password", }))
    # user_type = forms.ModelChoiceField(
    #     empty_label="Select roles ", queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'password1',)
