from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from apps.permissions.models import CustomUser
from apps.user.models import NormalUser
from apps.reviewer.models import Reviewer



def populate_models(sender, **kwargs):
    # below logic auto_create group 
    user_group, created = Group.objects.get_or_create(name='User')
    admin_group, created = Group.objects.get_or_create(name='Admin')
    reviewer_group, created = Group.objects.get_or_create(name='Reviewer')
    return [user_group, admin_group, reviewer_group]
    
    

@receiver(post_save, sender=CustomUser)
def create_authentication(sender, instance, created, **kwargs):  # instance is CustomUser
    if created:
        print("I am signal")
        group = populate_models(sender)
        if instance.user_type == group[0]:
            NormalUser.objects.create(normal_user=instance)
        if instance.user_type == group[2]:
                Reviewer.objects.create(reviewer_user=instance)
    
@receiver(post_save, sender=CustomUser)
def save_authentication(sender, instance, **kwargs):
    print("I am signal 2")
    group = populate_models(sender)
    if instance.user_type == group[0]: 
        instance.normaluser.save()
        print(instance)
    if instance.user_type == group[2]: 
        instance.reviewer.save()
