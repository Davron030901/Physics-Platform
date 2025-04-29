# amaliy/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PracticalTask
from .forms import PracticalTaskForm

def amaliy_list(request):
    tasks = PracticalTask.objects.all()
    return render(request, 'amaliy/amaliy_list.html', {'tasks': tasks})

def amaliy_detail(request, pk):
    task = get_object_or_404(PracticalTask, pk=pk)
    
    # Oldingi va keyingi ma'ruzalarni topish
    prev_task = PracticalTask.objects.filter(created_at__lt=task.created_at).order_by('-created_at').first()
    next_task = PracticalTask.objects.filter(created_at__gt=task.created_at).order_by('created_at').first()
    
    return render(request, 'amaliy/amaliy_detail.html', {
        'task': task,
        'prev_task': prev_task,
        'next_task': next_task
    })

@login_required
def amaliy_create(request):
    if request.method == 'POST':
        form = PracticalTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.teacher = request.user
            task.save()
            messages.success(request, "Amaliy mashg'ulot muvaffaqiyatli qo'shildi!")
            return redirect('amaliy_list')
    else:
        form = PracticalTaskForm()
    
    return render(request, 'amaliy/amaliy_form.html', {'form': form, 'action': 'create'})

@login_required
def amaliy_edit(request, pk):
    task = get_object_or_404(PracticalTask, pk=pk)
    
    if request.user != task.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu amaliy mashg'ulotni o'zgartira olmaysiz!")
        return redirect('amaliy_list')
    
    if request.method == 'POST':
        form = PracticalTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Amaliy mashg'ulot muvaffaqiyatli o'zgartirildi!")
            return redirect('amaliy_detail', pk=task.pk)
    else:
        form = PracticalTaskForm(instance=task)
    
    return render(request, 'amaliy/amaliy_form.html', {'form': form, 'task': task, 'action': 'edit'})

@login_required
def amaliy_delete(request, pk):
    task = get_object_or_404(PracticalTask, pk=pk)
    
    if request.user != task.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu amaliy mashg'ulotni o'chira olmaysiz!")
        return redirect('amaliy_list')
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Amaliy mashg'ulot muvaffaqiyatli o'chirildi!")
        return redirect('amaliy_list')
    
    return render(request, 'amaliy/amaliy_confirm_delete.html', {'task': task})