from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('create-post/', views.create_post, name='create_post')
    # path('post/<int:id>', views.delete_post, name='delete-post'),
]
