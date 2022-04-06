from django import forms

class coins_post_form(forms.Form):
    name = forms.CharField(max_length=15, label='Nombre')
    value = forms.FloatField(label='Valor')
    
    
    
class user_post_form(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')
    lastname = forms.CharField(max_length=20, label='Apellido')
    user_name = forms.CharField(max_length=20, label='Usuario')
    email = forms.EmailField(label='Correo Electrónico') 
    
    
    
class experience_post_form(forms.Form):
    user = forms.CharField(max_length=20, label='Nombre')
    ocupation = forms.CharField(max_length=10, label='Ocupación')
    experience = forms.CharField(max_length=150, label='Comentario')



class coin_search_form(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')