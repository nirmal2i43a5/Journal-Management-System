from django import forms
from django.utils.translation import gettext_lazy as _
from apps.permissions.models import CustomUser
from .models import *
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.core.exceptions import ValidationError

class CustomUserForm(forms.ModelForm):
    # password1 = forms.CharField(required = False, widget=forms.PasswordInput())
    # password2 = forms.CharField(required = False, widget=forms.PasswordInput())
    
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
         label=_("Password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
      
    class Meta:
        model = CustomUser
        fields = ('username','password1','password2',)
        
 

class UserRegisterForm(forms.ModelForm):
    dob = forms.DateField(required = False, label = 'Date of Birth', widget=forms.DateInput(attrs={'type': 'date', }))
    class Meta:
        model = NormalUser
        exclude = ('status','normal_user','image',)
        
        
class PaperUploadForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'