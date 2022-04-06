from django.urls import path
from . import views

urlpatterns = [
    path('', views.coins, name='coins'),
    path('post/', views.post_coins, name='post_coins'),
    path('experience/', views.post_experience, name='post_experience'),
    path('edit/<int:pk>', views.edit_coin.as_view(), name='edit_coin'),
    path('delete/<int:pk>', views.delete_coin.as_view(), name='delete_coin'),
    path('<int:pk>/', views.detail_coin.as_view(), name='detail_coin'),
]
