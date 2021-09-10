from django import forms
from django.utils.translation import gettext_lazy as _
from apps.permissions.models import CustomUser
from .models import *



class ReviewerRegisterForm(forms.ModelForm):
    dob = forms.DateField(required = False, label = 'Date of Birth', widget=forms.DateInput(attrs={'type': 'date', }))
    class Meta:
        model = Reviewer
        exclude = ('status','reviewer_user',)
        
        
class CustomUserForm(forms.ModelForm):
 
    class Meta:
        model = CustomUser
        fields = ('username',)
        exclude = ['password1','password2',]
        
 