from os import link
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .models import User_extension
from .forms import Edit_User, Project_user_form


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'msg': 'No se pudo ingresar'})
        else:
            return render(request, 'accounts/login.html', {'form': form, 'msg': 'El usuario no es válido'})
                
    
    form = AuthenticationForm() 
    return render(request, 'accounts/login.html', {'form': form, 'msg': None})


def signin(request):
    if request.method == 'POST':
        form = Project_user_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index/index.html', {'form': form, 'msg': ''})
        else:
            return render(request, 'accounts/signin.html', {'form': form, 'msg': 'El usuario no es válido'})
    form = Project_user_form()
    
    return render(request, 'accounts/signin.html', {'form': form, 'msg': None})

@login_required
def edit(request):
    logued_user = request.user
    logued_user_extension, _ = User_extension.objects.get_or_create(logued_user)
    
    if request.method == 'POST':
        form = Edit_User(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            logued_user_extension.avatar = data.get("avatar", '')
            logued_user_extension.link = data.get("link", '')
            logued_user.email = data.get('email', '')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1', ''):
                if len(data.get('password1')) >= 8:                
                    if data.get('password1')==data.get('password2'):
                        logued_user.set_password(data.get('password1'))
                    else: 
                        return render(request, 'accounts/edit_user.html', {'form': form, 'msg': 'Las contraseñas no coinciden', 'avatar_url': avatar_url(request.user)})             
                else: 
                    return render(request, 'accounts/edit_user.html', {'form': form, 'msg': 'La contraseña debe tener más de 8 caracteres', 'avatar_url': avatar_url(request.user)})             
            logued_user.save()
            logued_user_extension.save()
            return render(request, 'index/index.html', {'form': form, 'msg': '', 'avatar_url': avatar_url(request.user)})
        else:
            return render(request, 'accounts/edit_user.html', {'form': form, 'msg': 'El usuario no es válido', 'avatar_url': avatar_url(request.user)})
    form = Edit_User(
        initial={
            'email': logued_user.email,
            'first_name': logued_user.first_name,
            'last_name': logued_user.last_name,
            'link': logued_user_extension.link
        }
    )
    return render(request, 'accounts/edit_user.html', {'form': form, 'avatar_url': avatar_url(request.user)})

def avatar_url(user):
    try:
        return User_extension.objects.filter(user=user)[0].avatar.url
    except:
        return ""