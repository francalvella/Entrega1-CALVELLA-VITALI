from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import Edit_user, Project_user_form


# Create your views here.
def index(request):
    return render(request, 'index/index.html', {})

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
                return render(request, 'index/login.html', {'form': form, 'msg': 'No se pudo ingresar'})
        else:
            return render(request, 'index/login.html', {'form': form, 'msg': 'El usuario no es válido'})
                
    
    form = AuthenticationForm() 
    return render(request, 'index/login.html', {'form': form, 'msg': None})


def signin(request):
    if request.method == 'POST':
        form = Project_user_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index/index.html', {'form': form, 'msg': ''})
        else:
            return render(request, 'index/signin.html', {'form': form, 'msg': 'El usuario no es válido'})
    form = Project_user_form()
    
    return render(request, 'index/signin.html', {'form': form, 'msg': None})

@login_required
def edit(request):
    logued_user = request.user
    if request.method == 'POST':
        form = Edit_user(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logued_user.email = data.get('email', '')
            logued_user.first_name = data.get('first_name', '')
            logued_user.last_name = data.get('last_name', '')
            if data.get('password1', ''):
                if len(data.get('password1')) >= 8:                
                    if data.get('password1')==data.get('password2'):
                        logued_user.set_password(data.get('password1'))
                    else: 
                        return render(request, 'index/edit_user.html', {'form': form, 'msg': 'Las contraseñas no coinciden'})             
                else: 
                    return render(request, 'index/edit_user.html', {'form': form, 'msg': 'La contraseña debe tener más de 8 caracteres'})             
            logued_user.save()
            return render(request, 'index/index.html', {'form': form, 'msg': ''})
        else:
            return render(request, 'index/edit_user.html', {'form': form, 'msg': 'El usuario no es válido'})
    form = Edit_user(
        initial={
            'email': logued_user.email,
            'first_name': logued_user.first_name,
            'last_name': logued_user.last_name
        }
    )
    return render(request, 'index/edit_user.html', {'form': form})