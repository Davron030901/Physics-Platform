# sonmetodi/views.py
from django.shortcuts import render

def multiplication_game(request):
    return render(request, 'sonmetodi/multiplication_game.html')