from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category_images',null = True, blank = True)
    
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_category'
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Marquee(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.name