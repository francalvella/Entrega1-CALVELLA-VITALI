from django import forms
from ckeditor.fields import RichTextFormField
          
    
class Smart_Contracts_Post_Form(forms.Form):
    case = forms.CharField(max_length=15, label='Caso')
    info = RichTextFormField(required=False, label='Información')
    
class Smart_Contracts_Search_Form(forms.Form):
    name = forms.CharField(max_length=20, label='Caso', required=False)