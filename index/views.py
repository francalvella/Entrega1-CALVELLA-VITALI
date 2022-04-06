from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate


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