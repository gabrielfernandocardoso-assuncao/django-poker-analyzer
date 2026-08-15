from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-partida/', views.create_game, name='create_game'),
    path('partida/<int:game_id>/', views.game_panel, name='game_panel'),
    path('rebuy/<int:session_id>/', views.add_rebuy, name='add_rebuy')
]
