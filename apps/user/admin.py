from apps.permissions.models import CustomUser
from apps.user.models import Article, NormalUser
from django.contrib import admin
from apps.user.models import NormalUser, Article


# Register your models here.
admin.site.register(NormalUser)
admin.site.register(CustomUser)
admin.site.register(Article)


