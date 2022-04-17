from django.urls import path
from . import views

urlpatterns = [
    path('coins/', views.coins, name='coins'),
    path('coins/post/', views.post_coins, name='post_coins'),
    path('coins/experience/', views.post_experience, name='post_experience'),
    path('coins/edit/<int:pk>', views.edit_coin.as_view(), name='edit_coin'),
    path('coins/delete/<int:pk>', views.delete_coin.as_view(), name='delete_coin'),
    path('coins/<int:pk>/', views.detail_coin.as_view(), name='detail_coin'),
    path('nfts/', views.nfts, name='nfts'),
    path('nfts/experience/', views.post_nfts, name='post_nfts'),
    path('nfts/moreinfo/<int:pk>', views.detail_nfts.as_view(), name='detail_nfts'),

]
