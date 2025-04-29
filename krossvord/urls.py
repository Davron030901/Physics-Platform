# krossvord/urls.py
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    # Asosiy sahifa
    path('', views.crossword_list, name='crossword_list'),
    
    # So'z o'yini - yo'naltirish bilan
    path('word-game/', RedirectView.as_view(pattern_name='crossword_list'), name='word_game'),
    
    # Krossvord tafsilotlari
    path('<int:pk>/', views.crossword_detail, name='crossword_detail'),
    
    # Old views for compatibility
    path('word-game/play/', views.word_game, name='play_word_game'),
]