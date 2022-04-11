from django.db import models

# Create your models here.    

class Coin(models.Model):
    name = models.CharField(max_length=15)
    value = models.FloatField()
    
    def __str__(self):
        return f'{self.name}'
    
    
class Experience(models.Model):
    user = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=10)
    experience = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.user}'
    