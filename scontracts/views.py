from django.shortcuts import redirect, render
from .models import Smart_Contracts
from .forms import Smart_Contracts_Post_Form, Smart_Contracts_Search_Form
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required


# Create your views here.


def smart_contracts(request):
    search = request.GET.get('name', None)
    if search is not None:
        sc_array = Smart_Contracts.objects.filter(case__icontains=search)
    else:
        sc_array = Smart_Contracts.objects.all()
        
    form = Smart_Contracts_Search_Form()
    return render(request, 'smart_contracts/smart_contracts.html', {'form': form, 'sc_array': sc_array})

    
@login_required
def post_smart_contract(request):
    if request.method == 'POST':
        form = Smart_Contracts_Post_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            sc = Smart_Contracts(case=data['case'], info=data['info'], user=request.user)
            sc.save()
            return redirect('smart_contracts')
            
    form = Smart_Contracts_Post_Form()
    return render(request, 'smart_contracts/post_smart_contracts.html', {'form': form})


class Detail_Smart_Contracts(DetailView):
    model = Smart_Contracts
    template_name = 'smart_contracts/detail_smart_contracts.html'
    
    
