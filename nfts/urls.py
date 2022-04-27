from django.urls import path
from . import views

urlpatterns = [
    path('', views.nfts, name='nfts'),
    path('experience/', views.post_nfts, name='post_nfts'),
    path('moreinfo/<int:pk>', views.Detail_Nfts.as_view(), name='detail_nfts'),

]
