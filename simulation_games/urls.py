# simulation_games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('<int:pk>/', views.game_detail, name='game_detail'),
    path('create/', views.game_create, name='game_create'),
    path('<int:pk>/edit/', views.game_edit, name='game_edit'),
    path('<int:pk>/delete/', views.game_delete, name='game_delete'),
]