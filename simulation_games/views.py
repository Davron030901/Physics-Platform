# simulation_games/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect
from .models import SimulationGame
from .forms import SimulationGameForm

def is_staff(user):
    return user.is_staff

def game_list(request):
    games = SimulationGame.objects.filter(is_active=True)
    return render(request, 'simulation_games/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(SimulationGame, pk=pk, is_active=True)
    return render(request, 'simulation_games/game_detail.html', {'game': game})

@login_required
@user_passes_test(is_staff)
def game_create(request):
    if request.method == 'POST':
        form = SimulationGameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
            messages.success(request, "Simulyatsion o'yin muvaffaqiyatli qo'shildi!")
            return redirect('game_list')
    else:
        form = SimulationGameForm()
    
    return render(request, 'simulation_games/game_form.html', {'form': form, 'action': 'create'})

@login_required
@user_passes_test(is_staff)
def game_edit(request, pk):
    game = get_object_or_404(SimulationGame, pk=pk)
    
    if request.method == 'POST':
        form = SimulationGameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            messages.success(request, "Simulyatsion o'yin muvaffaqiyatli yangilandi!")
            return redirect('game_detail', pk=game.pk)
    else:
        form = SimulationGameForm(instance=game)
    
    return render(request, 'simulation_games/game_form.html', {'form': form, 'game': game, 'action': 'edit'})

@login_required
@user_passes_test(is_staff)
def game_delete(request, pk):
    game = get_object_or_404(SimulationGame, pk=pk)
    
    if request.method == 'POST':
        game.delete()
        messages.success(request, "Simulyatsion o'yin muvaffaqiyatli o'chirildi!")
        return redirect('game_list')
    
    return render(request, 'simulation_games/game_confirm_delete.html', {'game': game})