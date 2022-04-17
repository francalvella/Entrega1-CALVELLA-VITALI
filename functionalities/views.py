from django.shortcuts import redirect, render

from functionalities.models import Coin, Experience, NFTs
from .forms import NFTS_post_form, coin_search_form, coins_post_form, experience_post_form, nfts_search_form
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import avatar_url


# Create your views here.

def coins(request):
    search = request.GET.get('name', None)
    if search is not None:
        coins_array = Coin.objects.filter(name__icontains=search)
    else:
        coins_array = Coin.objects.all()
        
    form = coin_search_form()
    return render(request, 'functionalities/coins.html', {'form': form, 'coins_array': coins_array, 'avatar_url': avatar_url(request.user)})

    
def nfts(request):
    search = request.GET.get('user', None)
    if search is not None:
        nfts_array = NFTs.objects.filter(user__icontains=search)
    else:
        nfts_array = NFTs.objects.all()
        
    form = nfts_search_form()
    return render(request, 'functionalities/nfts.html', {'form': form, 'nfts_array': nfts_array, 'avatar_url': avatar_url(request.user)})


@login_required
def post_coins(request):
    if request.method == 'POST':
        form = coins_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            coin = Coin(name=data['name'], value=data['value'], info=data['info'])
            coin.save()
            return redirect('coins')
            
    form = coins_post_form()
    return render(request, 'functionalities/post_coins.html', {'form': form, 'avatar_url': avatar_url(request.user)})

    
@login_required
def post_nfts(request):
    if request.method == 'POST':
        form = NFTS_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nft = NFTs(user=request.user, title=data['title'], info=data['info'])
            nft.save()
            return redirect('nfts')
            
    form = NFTS_post_form()
    return render(request, 'functionalities/post_nfts.html', {'form': form, 'avatar_url': avatar_url(request.user)})


@login_required
def post_experience(request):
    experiences_array = Experience.objects.all()
    
    if request.method == 'POST':
        form = experience_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Experience(user=request.user, ocupation=data['ocupation'], experience=data['experience'])
            review.save()
            return render(request, 'functionalities/experience.html', {'form': form, 'experiences_array': experiences_array, 'avatar_url': avatar_url(request.user)})
            
    
    form = experience_post_form
    return render(request, 'functionalities/experience.html', {'form': form, 'experiences_array': experiences_array, 'avatar_url': avatar_url(request.user)})


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
    fields = ['name', 'value', 'info' ]


class detail_nfts(DetailView):
    model = NFTs
    template_name = 'functionalities/detail_nfts.html'
