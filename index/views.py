from django.shortcuts import render
from accounts.views import avatar_url

# Create your views here.
def index(request):
    return render(request, 'index/index.html', {'avatar_url': avatar_url(request.user)})

def about(request):
    return render(request, 'index/about.html', {'avatar_url': avatar_url(request.user)})