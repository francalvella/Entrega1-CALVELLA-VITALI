from django import forms
from ckeditor.fields import RichTextFormField
      
class NFTS_Post_Form(forms.Form):
    title = forms.CharField(max_length=15, label='Titulo')
    info = RichTextFormField()

class Nfts_Search_Form(forms.Form):
    name = forms.CharField(max_length=20, label='Buscar', required=False)
