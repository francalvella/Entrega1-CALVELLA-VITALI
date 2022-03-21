import email
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.EmailField() 

class Coin(models.Model):
    name = models.CharField(max_length=15)
    value = models.FloatField()
    
class Experience(models.Model):
    user_name = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=10)
    experience = models.CharField(max_length=150)
