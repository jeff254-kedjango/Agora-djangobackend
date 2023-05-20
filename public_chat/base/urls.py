from django.urls import path
from . import views

urlpatterns = [
    path('', views.public_feed, name='feed'),
    path('add/', views.add_post),
]