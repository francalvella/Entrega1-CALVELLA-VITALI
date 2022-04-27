from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=15)
    value = models.FloatField()
    info = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Experience(models.Model):
    user = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=20)
    experience = RichTextField(default='No se ha cargado información')

    def __str__(self):
        return f'{self.user}'    