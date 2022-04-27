from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=80)
    info = RichTextField(default='No hay información aún')
    image = models.ImageField(upload_to='media_stge',blank=True, null=True) 
    user = models.CharField(max_length=15)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title}'