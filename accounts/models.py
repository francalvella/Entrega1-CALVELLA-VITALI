from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtension(models.Model):
    avatar = models.ImageField(upload_to='avatars',blank=True, null=True, default="avatars/Bitcoin-Logo.png")
    link = models.URLField(max_length=200, default='', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
   