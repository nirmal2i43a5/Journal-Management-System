from django import forms
from .models import *
        
class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
 