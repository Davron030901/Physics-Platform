# krossvord/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WordGame, Crossword, CrosswordClue
import random

def crossword_list(request):
    crosswords = Crossword.objects.all()
    return render(request, 'krossvord/crossword_list.html', {'crosswords': crosswords})

def crossword_detail(request, pk):
    crossword = get_object_or_404(Crossword, pk=pk)
    
    # Savollarni yo'nalishi bo'yicha ajratish
    across_clues = crossword.clues.filter(direction='across').order_by('number')
    down_clues = crossword.clues.filter(direction='down').order_by('number')
    
    return render(request, 'krossvord/crossword_detail.html', {
        'crossword': crossword,
        'across_clues': across_clues,
        'down_clues': down_clues
    })

def word_game(request):
    games = list(WordGame.objects.all())
    
    if not games:
        return render(request, 'krossvord/word_game.html', {'no_games': True})
    
    game = random.choice(games)
    
    return render(request, 'krossvord/word_game.html', {'game': game})