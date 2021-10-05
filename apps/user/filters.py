import django_filters
from django.utils.translation import gettext_lazy as _
from .models import Article
from apps.admin_user.models import Category


class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name = "title",lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'category']