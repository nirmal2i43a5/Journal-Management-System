from apps.permissions.models import CustomUser
from apps.user.models import NormalUser
from django.contrib import admin
from apps.user.models import NormalUser
from apps.permissions.models  import CustomUser

# Register your models here.
admin.site.register(NormalUser)
admin.site.register(CustomUser)