from django.urls import path
from .views import Detail_Smart_Contracts, post_smart_contract, smart_contracts

urlpatterns = [
    path('', smart_contracts, name='smart_contracts'),
    path('experience/', post_smart_contract, name='post_smart_contracts'),
    path('moreinfo/<int:pk>', Detail_Smart_Contracts.as_view(), name='detail_smart_contracts'),

]
