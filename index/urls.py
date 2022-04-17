from django.urls import path, include
from .views import index, about


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('pages/', include('functionalities.urls')),
    path('accounts/', include('accounts.urls'))
    ]
