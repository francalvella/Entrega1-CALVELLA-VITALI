from django.shortcuts import redirect, render
from .models import Article
from .forms import Article_Post_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.

def article(request):
    article_array = Article.objects.all()
    return render(request, 'articles/article.html', {'article_array': article_array})


@login_required
def post_article(request):
    
    if request.method == 'POST':
        form = Article_Post_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            article = Article(user=request.user, title=data['title'], subtitle=data['subtitle'], info=data['info'], image=data['image'])
            article.save()
            return redirect('article')
            
    
    form = Article_Post_Form()
    return render(request, 'articles/post_article.html', {'form': form})

class Edit_Article(LoginRequiredMixin, UpdateView):
    model = Article
    success_url = '/pages/'
    fields = ['title', 'subtitle', 'info', 'image' ]

class Delete_Article(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/pages'
    fields = ['title', 'subtitle', 'info', 'image', 'user', 'date']
    template_name = 'articles/confirm_delete.html'

class Detail_Article(DetailView):
    model = Article
    template_name = 'articles/detail_article.html'
