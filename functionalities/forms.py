from django import forms
from ckeditor.fields import RichTextFormField

class coins_post_form(forms.Form):
    name = forms.CharField(max_length=15, label='Nombre')
    value = forms.FloatField(label='Valor')
    info = RichTextFormField(required=False)
    
    
class NFTS_post_form(forms.Form):
    title = forms.CharField(max_length=15, label='Titulo')
    info = RichTextFormField()
    
    
class Smart_contracts_post_form(forms.Form):
    case = forms.CharField(max_length=15, label='Caso')
    info = RichTextFormField(required=False, label='Información del caso')
    
    
    
class experience_post_form(forms.Form):
    ocupation = forms.CharField(max_length=10, label='Ocupación')
    experience = forms.CharField(max_length=150, label='Comentario')



class coin_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')

class nfts_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Buscar')

class smart_contracts_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Caso')