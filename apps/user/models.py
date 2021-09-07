from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.permissions.models import CustomUser
from apps.admin_user.models import Category





class NormalUser(models.Model):
    
    gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Third Gender', 'Third Gender')
)

    # institution
    # department
    # bio
    
    normal_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length = 250, blank=True)
    email = models.EmailField()
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=20, choices=gender_choice, default='Male', blank=True)
    contact = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_normal_user'
        verbose_name = _("normal_user")
        verbose_name_plural = _("normal_user")

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        
class Journal(models.Model):
    file = models.FileField(upload_to='Journal_papers', null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    new_category = models.CharField(help_text = 'Only add new Category if you do not see your wise category in Category Choice list.',max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_journal'
        verbose_name = _("journal")
        verbose_name_plural = _("journals")