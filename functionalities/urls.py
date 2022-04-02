from django.urls import path
from . import views

urlpatterns = [
    path('', views.coins, name='coins'),
    path('post/', views.post_coins, name='post_coins'),
    path('experience/', views.post_experience, name='post_experience'),
]
