from django.urls import path
from . import views

urlpatterns = [
    path('', views.coins, name='coins'),
    path('post/', views.post_coins, name='post_coins'),
    path('login/', views.post_user, name='post_user'),
    path('experience/', views.post_experience, name='post_experience'),
]
