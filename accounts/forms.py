from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectUserForm(UserCreationForm):
    
    email = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { k: '' for k in fields}


class EditUser(forms.Form):
    avatar = forms.ImageField(required=False)
    email = forms.CharField()
    first_name = forms.CharField(max_length=20, label='Nombre', required=False)
    last_name = forms.CharField(max_length=20, label='Apellido', required=False)
    link = forms.URLField(max_length=200, required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(), required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(), required=False)
    