from django.shortcuts import redirect, render
from .forms import NFTS_Post_Form, Nfts_Search_Form
from .models import NFTs
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


# Create your views here.

def nfts(request):
    search = request.GET.get('name', None)
    if search is not None:
        nfts_array = NFTs.objects.filter(title__icontains=search)
    else:
        nfts_array = NFTs.objects.all()
        
    form = Nfts_Search_Form()
    return render(request, 'nfts/nfts.html', {'form': form, 'nfts_array': nfts_array})


@login_required
def post_nfts(request):
    if request.method == 'POST':
        form = NFTS_Post_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nft = NFTs(user=request.user, title=data['title'], info=data['info'])
            nft.save()
            return redirect('nfts')
            
    form = NFTS_Post_Form()
    return render(request, 'nfts/post_nfts.html', {'form': form})


class Detail_Nfts(DetailView):
    model = NFTs
    template_name = 'nfts/detail_nfts.html'
