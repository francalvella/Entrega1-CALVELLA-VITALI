from django import forms
from ckeditor.fields import RichTextFormField

class Article_Post_Form(forms.Form):
    title = forms.CharField(max_length=20)
    subtitle = forms.CharField(max_length=80)
    info = RichTextFormField()
    image = forms.ImageField() 
