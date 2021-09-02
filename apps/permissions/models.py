from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# from ckeditor.fields import RichTextField
from django.contrib.auth.models import Group


class CustomUser(AbstractUser):
    
    user_type = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_Customuser'
        verbose_name = _("customuser")
        verbose_name_plural = _("customusers")

    def __str__(self):
        return self.user_type

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)