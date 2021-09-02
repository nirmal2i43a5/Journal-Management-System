from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

admin_group, created = Group.objects.get_or_create(name='Admin')
user_group, created = Group.objects.get_or_create(name='User')
reviewer_group, created = Group.objects.get_or_create(name='Reviewer')