import email
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email = models.EmailField() 
    
    def __str__(self):
        return f'{self.user_name}'
    

class Coin(models.Model):
    name = models.CharField(max_length=15)
    value = models.FloatField()
    
    def __str__(self):
        return f'{self.name} - {self.value} U$D'
    
    
class Experience(models.Model):
    user = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=10)
    experience = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.user}'
    