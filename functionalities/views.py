from django.shortcuts import redirect, render

from functionalities.models import Coin, Experience, User
from .forms import coin_search_form, coins_post_form, experience_post_form, user_post_form

# Create your views here.

def coins(request):
    search = request.GET.get('name', None)
    if search is not None:
        coins_array = Coin.objects.filter(name__icontains=search)
    else:
        coins_array = Coin.objects.all()
        
    form = coin_search_form()
    return render(request, 'functionalities/coins.html', {'form': form, 'coins_array': coins_array})



def post_coins(request):
    if request.method == 'POST':
        form = coins_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            coin = Coin(name=data['name'], value=data['value'])
            coin.save()
            return redirect('coins')
            
    form = coins_post_form()
    return render(request, 'functionalities/post_coins.html', {'form': form})



def post_user(request):
    if request.method == 'POST':
        form = user_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(name=data['name'], lastname=data['lastname'], user_name=data['user_name'], email=data['email'])
            user.save()
            return redirect('index')
            
    
    form = user_post_form
    return render(request, 'functionalities/users.html', {'form': form})


def post_experience(request):
    experiences_array = Experience.objects.all()
    
    if request.method == 'POST':
        form = experience_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Experience(user=data['user'], ocupation=data['ocupation'], experience=data['experience'])
            review.save()
            return render(request, 'functionalities/experience.html', {'form': form, 'experiences_array': experiences_array})
            
    
    form = experience_post_form
    return render(request, 'functionalities/experience.html', {'form': form, 'experiences_array': experiences_array})