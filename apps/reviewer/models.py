from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.permissions.models import CustomUser
from apps.admin_user.models import Category




STATUS_UNSUBMITTED = 'Unsubmitted'
STATUS_UNDER_REVIEW = 'Under Review'
STATUS_REJECTED = 'Rejected'
STATUS_ACCEPTED = 'Accepted'
STATUS_REVIEWER_PUBLISHED = 'Reviewer Published'
STATUS_ADMIN_PUBLISHED = 'Admin Published'
STATUS_CHOICES = [
    (STATUS_UNSUBMITTED, 'Unsubmitted'),
    (STATUS_UNDER_REVIEW, 'Peer Review'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_ACCEPTED, 'Accepted'),
    (STATUS_REVIEWER_PUBLISHED, 'Reviewer Published'),
    (STATUS_ADMIN_PUBLISHED, 'Admin Published'),
]


class Reviewer(models.Model):
    
    gender_choice = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Third Gender', 'Third Gender')
)

    reviewer_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
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
        db_table = 'tbl_reviewer'
        verbose_name = _("reviewer")
        verbose_name_plural = _("reviewer")

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        