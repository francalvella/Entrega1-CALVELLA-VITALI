from django import forms
from ckeditor.fields import RichTextFormField

class CoinsPostForm(forms.Form):
    name = forms.CharField(max_length=15, label='Nombre')
    value = forms.FloatField(label='Valor')
    info = RichTextFormField(required=False)

class ExperiencePostForm(forms.Form):
    ocupation = forms.CharField(max_length=20, label='Ocupación')
    experience = RichTextFormField(label='Comentario')

class CoinSearchForm(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre', required=False)
