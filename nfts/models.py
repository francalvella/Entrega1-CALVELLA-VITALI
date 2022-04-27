from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class NFTs(models.Model):
    user = models.CharField(max_length=15)
    title = models.CharField(max_length=15)
    info = RichTextField(default='No se ha cargado información')
    
    def __str__(self):
        return f'{self.title}'