from django.urls import path
from . import views

urlpatterns = [
    path('', views.article, name='article'),
    path('post/', views.post_article, name='post_article'),
    path('edit/<int:pk>', views.Edit_Article.as_view(), name='edit_article'),
    path('delete/<int:pk>', views.Delete_Article.as_view(), name='delete_article'),
    path('page/<int:pk>', views.Detail_Article.as_view(), name='detail_article')


]
