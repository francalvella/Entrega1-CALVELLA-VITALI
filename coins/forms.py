from django import forms
from ckeditor.fields import RichTextFormField

class Coins_Post_Form(forms.Form):
    name = forms.CharField(max_length=15, label='Nombre')
    value = forms.FloatField(label='Valor')
    info = RichTextFormField(required=False)

class Experience_Post_Form(forms.Form):
    ocupation = forms.CharField(max_length=20, label='Ocupación')
    experience = RichTextFormField(label='Comentario')

class Coin_Search_Form(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre', required=False)
