from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.    

class Smart_Contracts(models.Model):
    case = models.CharField(max_length=40)
    info = RichTextField(default='No se ha cargado información')
    user = models.CharField(max_length=20, default='Desconocido')
    
    def __str__(self):
        return f'{self.case}'
    
