from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='article'),
    path('coins/', views.coins, name='coins'),
    path('nfts/', views.nfts, name='nfts'),
    path('smart-contracts/', views.smart_contracts, name='smart_contracts'),
    path('coins/experience/', views.post_experience, name='post_experience'),
    path('post/', views.post_article, name='post_article'),
    path('coins/post/', views.post_coins, name='post_coins'),
    path('smart-contracts/experience/', views.post_smart_contract, name='post_smart_contracts'),
    path('nfts/experience/', views.post_nfts, name='post_nfts'),
    path('coins/edit/<int:pk>', views.edit_coin.as_view(), name='edit_coin'),
    path('coins/<int:pk>/', views.detail_coin.as_view(), name='detail_coin'),
    path('nfts/moreinfo/<int:pk>', views.detail_nfts.as_view(), name='detail_nfts'),
    path('moreinfo/<int:pk>', views.detail_article.as_view(), name='detail_article'),
    path('smart-contracts/moreinfo/<int:pk>', views.detail_smart_contracts.as_view(), name='detail_smart_contracts'),
    path('coins/experience/delete/<int:pk>', views.delete_experience.as_view(), name='delete_experience'),
    path('delete/<int:pk>', views.delete_article.as_view(), name='delete_article'),
    path('coins/delete/<int:pk>', views.delete_coin.as_view(), name='delete_coin'),

]
