from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-partida/', views.create_game, name='create_game'),
]
