from django.urls import path, include
import functionalities
from .views import edit, index, login_view, signin
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', index, name='index'),
    path('login/',login_view, name='login'),
    path('signin/',signin, name='signin'),
    path('coins/', include('functionalities.urls')),
    path('logout/', LogoutView.as_view(template_name='index/logout.html'), name='logout'), 
    path('edit/', edit, name='edit')
]
