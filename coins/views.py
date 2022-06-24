from django.shortcuts import render, redirect
from .models import Coin, Experience
from .forms import CoinSearchForm, CoinsPostForm, ExperiencePostForm
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
        
    form = CoinSearchForm()
    return render(request, 'coins/coins.html', {'form': form, 'coins_array': coins_array})


@login_required
def post_coins(request):
    if request.method == 'POST':
        form = CoinsPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            coin = Coin(name=data['name'], value=data['value'], info=data['info'])
            coin.save()
            return redirect('coins')
            
    form = CoinsPostForm()
    return render(request, 'coins/post_coins.html', {'form': form})


@login_required
def post_experience(request):
    experiences_array = Experience.objects.all()
    
    if request.method == 'POST':
        form = ExperiencePostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Experience(user=request.user, ocupation=data['ocupation'], experience=data['experience'])
            review.save()
            return redirect('post_experience')
            
    
    form = ExperiencePostForm
    return render(request, 'coins/experience.html', {'form': form, 'experiences_array': experiences_array})

class DetailCoin(DetailView):
    model = Coin
    template_name = 'coins/detail_coin.html'

class DeleteCoin(LoginRequiredMixin, DeleteView):
    model = Coin
    success_url = '/coins/'
    fields = ['name', 'value' ]
    template_name = 'coins/confirm_delete.html'


class DeleteExperience(LoginRequiredMixin, DeleteView):
    model = Experience
    success_url = '/coins/experience/'
    fields = ['user', 'ocupation', 'experience' ]
    template_name = 'coins/confirm_delete.html'

class EditCoin(LoginRequiredMixin, UpdateView):
    model = Coin
    success_url = '/coins/'
    fields = ['name', 'value', 'info' ]
