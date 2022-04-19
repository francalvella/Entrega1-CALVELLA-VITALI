from django.contrib import admin
from .models import Article, Coin, Experience, NFTs, Smart_Contracts
# Register your models here.
admin.site.register(Coin)
admin.site.register(Experience)
admin.site.register(NFTs)
admin.site.register(Smart_Contracts)
admin.site.register(Article)
