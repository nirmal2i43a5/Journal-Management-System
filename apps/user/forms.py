from django import forms
from apps.permissions.models import CustomUser
from .models import *

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(required = False, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required = False, widget=forms.PasswordInput())
      
    class Meta:
        model = CustomUser
        fields = ('username','password','confirm_password',)
        


class UserRegisterForm(forms.ModelForm):
    dob = forms.DateField(required = False, label = 'Date of Birth', widget=forms.DateInput(attrs={'type': 'date', }))
    class Meta:
        model = NormalUser
        exclude = ('status','normal_user','image',)