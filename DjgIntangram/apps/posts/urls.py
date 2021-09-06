#Django
from django.urls import path
#Views
from . import views

urlpatterns = [
    path('', views.posts_list, name='feed'),
    path('post/new/', views.create_post, name='create_post'),
]
