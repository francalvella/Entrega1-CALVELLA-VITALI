from django.shortcuts import redirect, render

from functionalities.models import Coin, Experience
from .forms import coin_search_form, coins_post_form, experience_post_form, user_post_form
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def coins(request):
    search = request.GET.get('name', None)
    if search is not None:
        coins_array = Coin.objects.filter(name__icontains=search)
    else:
        coins_array = Coin.objects.all()
        
    form = coin_search_form()
    return render(request, 'functionalities/coins.html', {'form': form, 'coins_array': coins_array})


@login_required
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


@login_required
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


class detail_coin(DetailView):
    model = Coin
    template_name = 'functionalities/detail_coin.html'


class delete_coin(LoginRequiredMixin, DeleteView):
    model = Coin
    success_url = '/coins'
    fields = ['name', 'value' ]


class edit_coin(LoginRequiredMixin, UpdateView):
    model = Coin
    success_url = '/coins'
    fields = ['name', 'value' ]
