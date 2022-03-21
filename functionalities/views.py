from django.shortcuts import render

# Create your views here.

def coins(request):
    return render(request, 'functionalities/coins.html', {})