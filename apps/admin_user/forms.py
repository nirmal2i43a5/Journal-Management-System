from django import forms
from .models import *
        
class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class MarqueeForm(forms.ModelForm):
    class Meta:
        model = Marquee
        fields = '__all__'
        
 