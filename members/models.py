from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profiles', null=True, blank=True)
    bio = models.TextField(default='I LOVE MUSIC!')
    birthdate = models.DateField(null=True)
    

def create_profile_auto(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
    
post_save.connect(create_profile_auto, sender=User)