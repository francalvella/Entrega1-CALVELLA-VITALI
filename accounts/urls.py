from django.urls import path
from .views import edit, login_view, profile, signin
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',login_view, name='login'),
    path('signin/',signin, name='signin'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'), 
    path('profile/edit', edit, name='edit'),
    path('profile', profile, name='profile')
]

