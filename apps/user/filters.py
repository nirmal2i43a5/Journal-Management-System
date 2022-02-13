import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Article
from apps.admin_user.models import Category
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name = "title",lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'category']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('title', css_class='form-group col-md-4 mb-0'),
    #             Column('category', css_class='form-group col-md-4 mb-0'),
    #             css_class='form-row'
    #         ),
    #     )  