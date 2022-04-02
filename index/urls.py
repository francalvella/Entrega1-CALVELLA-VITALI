from django.urls import path, include

import functionalities
from .views import index
from functionalities.views import post_user

urlpatterns = [
    path('', index, name='index'),
    path('login/', functionalities.views.post_user, name='post_user'),
    path('coins/', include('functionalities.urls')),
    
]
