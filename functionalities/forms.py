from django import forms
from ckeditor.fields import RichTextFormField

class coins_post_form(forms.Form):
    name = forms.CharField(max_length=15, label='Nombre')
    value = forms.FloatField(label='Valor')
    info = RichTextFormField(required=False)
    
    
class NFTS_post_form(forms.Form):
    title = forms.CharField(max_length=15, label='Titulo')
    info = RichTextFormField()
    
    
class smart_contracts_post_form(forms.Form):
    case = forms.CharField(max_length=15, label='Caso')
    info = RichTextFormField(required=False, label='Información')
    
class article_post_form(forms.Form):
    title = forms.CharField(max_length=20)
    subtitle = forms.CharField(max_length=80)
    info = RichTextFormField()
    image = forms.ImageField() 
    
    
    
class experience_post_form(forms.Form):
    ocupation = forms.CharField(max_length=20, label='Ocupación')
    experience = RichTextFormField(label='Comentario')



class coin_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre', required=False)

class nfts_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Buscar', required=False)

class smart_contracts_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Caso', required=False)