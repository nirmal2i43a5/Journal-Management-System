from django.db import models
from django.db.models.fields import BooleanField
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.permissions.models import CustomUser
from apps.admin_user.models import Category




STATUS_UNSUBMITTED = 'Unsubmitted'
STATUS_UNDER_REVIEW = 'Under Review'
STATUS_REJECTED = 'Rejected'
STATUS_ACCEPTED = 'Accepted'
STATUS_PUBLISHED = 'Published'
STATUS_CHOICES = [
    (STATUS_UNSUBMITTED, 'Unsubmitted'),
    (STATUS_UNDER_REVIEW, 'Peer Review'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_ACCEPTED, 'Accepted'),
    (STATUS_PUBLISHED, 'Published'),
]



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
    full_name = models.CharField(max_length = 250)
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
        
        
class Article(models.Model):
    file = models.FileField(upload_to='Journal_papers', null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank = True)
    new_category = models.CharField(help_text = 'Only add new Category if you do not see your wise category in Category Choice list.',max_length=100,null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tbl_article'
        verbose_name = _("article")
        verbose_name_plural = _("articles")
        
        

class Feedback(models.Model):
    status = (
        ('Accepted','Accepted'),('Rejected','Rejected')
    )
    status = models.CharField(max_length=50,choices = status, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank = True)