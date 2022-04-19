from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.    

class Coin(models.Model):
    name = models.CharField(max_length=15)
    value = models.FloatField()
    info = RichTextField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'

    
class NFTs(models.Model):
    user = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    info = RichTextField(default='No se ha cargado información')
    
    def __str__(self):
        return f'{self.title}'
    

class Smart_Contracts(models.Model):
    case = models.CharField(max_length=40)
    info = RichTextField(default='No se ha cargado información')
    user = models.CharField(max_length=20, default='Desconocido')
    
    def __str__(self):
        return f'{self.case}'
    
    
class Experience(models.Model):
    user = models.CharField(max_length=20)
    ocupation = models.CharField(max_length=20)
    experience = RichTextField(default='No se ha cargado información')

    def __str__(self):
        return f'{self.user}'
    
    
class Article(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=80)
    info = RichTextField(default='No hay información aún')
    image = models.ImageField(upload_to='media_stge',blank=True, null=True) 
    user = models.CharField(max_length=15)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title}'