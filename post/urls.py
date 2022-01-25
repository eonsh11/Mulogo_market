from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('create-post/', views.create_post, name='create-post'),
    # path('main/delete/<int:id>', views.delete_tweet, name='delete-tweet'),
    # path('main/<int:id>', views.detail_tweet, name='detail-tweet'),
    # path('main/comment/<int:id>',views.write_comment, name='write-comment'),
    # path('main/comment/delete/<int:id>',views.delete_comment, name='delete-comment'),
    # path('post/<int:id>', views.delete_post, name='delete-post'),
]
