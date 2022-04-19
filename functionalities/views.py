from django.shortcuts import redirect, render

from functionalities.models import Article, Coin, Experience, NFTs, Smart_Contracts
from .forms import NFTS_post_form, article_post_form, coin_search_form, coins_post_form, experience_post_form, nfts_search_form, smart_contracts_post_form, smart_contracts_search_form
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
    search = request.GET.get('name', None)
    if search is not None:
        nfts_array = NFTs.objects.filter(title__icontains=search)
    else:
        nfts_array = NFTs.objects.all()
        
    form = nfts_search_form()
    return render(request, 'functionalities/nfts.html', {'form': form, 'nfts_array': nfts_array, 'avatar_url': avatar_url(request.user)})


def smart_contracts(request):
    search = request.GET.get('name', None)
    if search is not None:
        sc_array = Smart_Contracts.objects.filter(case__icontains=search)
    else:
        sc_array = Smart_Contracts.objects.all()
        
    form = smart_contracts_search_form()
    return render(request, 'functionalities/smart_contracts.html', {'form': form, 'sc_array': sc_array, 'avatar_url': avatar_url(request.user)})


def article(request):
    article_array = Article.objects.all()
    return render(request, 'functionalities/article.html', {'article_array': article_array, 'avatar_url': avatar_url(request.user), 'article_img_url': article_img_url(Article.title)})


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
def post_smart_contract(request):
    if request.method == 'POST':
        form = smart_contracts_post_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sc = Smart_Contracts(case=data['case'], info=data['info'], user=request.user)
            sc.save()
            return redirect('smart_contracts')
            
    form = smart_contracts_post_form()
    return render(request, 'functionalities/post_smart_contracts.html', {'form': form, 'avatar_url': avatar_url(request.user)})


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



@login_required
def post_article(request):
    
    if request.method == 'POST':
        form = article_post_form(request.POST, request.FILES)
        if form.is_valid():
            article_array = Article.objects.all()
            data = form.cleaned_data
            article = Article(user=request.user, title=data['title'], subtitle=data['subtitle'], info=data['info'], image=data['image'])
            article.save()
            return render(request, 'functionalities/article.html', {'form': form, 'article_array': article_array, 'avatar_url': avatar_url(request.user)})
            
    
    form = article_post_form()
    return render(request, 'functionalities/post_article.html', {'form': form, 'avatar_url': avatar_url(request.user)})


class detail_coin(DetailView):
    model = Coin
    template_name = 'functionalities/detail_coin.html'

class detail_article(DetailView):
    model = Article
    template_name = 'functionalities/detail_article.html'


class delete_coin(LoginRequiredMixin, DeleteView):
    model = Coin
    success_url = '/pages/coins'
    fields = ['name', 'value' ]
    template_name = 'functionalities/confirm_delete.html'

class delete_article(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/pages'
    fields = ['title', 'subtitle', 'info', 'image', 'user', 'date']
    template_name = 'functionalities/confirm_delete.html'

class delete_experience(LoginRequiredMixin, DeleteView):
    model = Experience
    success_url = '/pages/coins/experience/'
    fields = ['user', 'ocupation', 'experience' ]
    template_name = 'functionalities/confirm_delete.html'

class edit_coin(LoginRequiredMixin, UpdateView):
    model = Coin
    success_url = '/pages/coins'
    fields = ['name', 'value', 'info' ]


class detail_nfts(DetailView):
    model = NFTs
    template_name = 'functionalities/detail_nfts.html'

class detail_smart_contracts(DetailView):
    model = Smart_Contracts
    template_name = 'functionalities/detail_smart_contracts.html'
    
def article_img_url(title):
    try:
        return Article.objects.filter(title=title)[0].image.url
    except:
        return ""
    
