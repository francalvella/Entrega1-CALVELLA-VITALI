from django.urls import path
from . import views

urlpatterns = [
    path('', views.coins, name='coins'),
    path('experience/', views.post_experience, name='post_experience'),
    path('post/', views.post_coins, name='post_coins'),
    path('edit/<int:pk>', views.EditCoin.as_view(), name='edit_coin'),
    path('<int:pk>/', views.DetailCoin.as_view(), name='detail_coin'),
    path('experience/delete/<int:pk>', views.DeleteExperience.as_view(), name='delete_experience'),
    path('delete/<int:pk>', views.DeleteCoin.as_view(), name='delete_coin'),

]
