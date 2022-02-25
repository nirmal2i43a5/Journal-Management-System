from django import forms
from .models import *
        
class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice            
        fields = ['title','file','description']