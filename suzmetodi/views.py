# suzmetodi/views.py
from django.shortcuts import render
from krossvord.models import WordGame
import random

def suz_game(request):
    games = list(WordGame.objects.all())
    
    if not games:
        return render(request, 'suzmetodi/suz_game.html', {'no_games': True})
    
    game = random.choice(games)
    
    return render(request, 'suzmetodi/suz_game.html', {'game': game})