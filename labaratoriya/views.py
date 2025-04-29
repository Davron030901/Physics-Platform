# labaratoriya/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Laboratory
from .forms import LaboratoryForm

def labaratoriya_list(request):
    labs = Laboratory.objects.all()
    return render(request, 'labaratoriya/labaratoriya_list.html', {'labs': labs})

def labaratoriya_detail(request, pk):
    lab = get_object_or_404(Laboratory, pk=pk)
    
    # Oldingi va keyingi laboratoriya ishlarini topish
    prev_lab = Laboratory.objects.filter(created_at__lt=lab.created_at).order_by('-created_at').first()
    next_lab = Laboratory.objects.filter(created_at__gt=lab.created_at).order_by('created_at').first()
    
    return render(request, 'labaratoriya/labaratoriya_detail.html', {
        'lab': lab,
        'prev_lab': prev_lab,
        'next_lab': next_lab
    })

@login_required
def labaratoriya_create(request):
    if request.method == 'POST':
        form = LaboratoryForm(request.POST, request.FILES)
        if form.is_valid():
            lab = form.save(commit=False)
            lab.teacher = request.user
            lab.save()
            messages.success(request, "Laboratoriya ishi muvaffaqiyatli qo'shildi!")
            return redirect('labaratoriya_list')
    else:
        form = LaboratoryForm()
    
    return render(request, 'labaratoriya/labaratoriya_form.html', {'form': form, 'action': 'create'})

@login_required
def labaratoriya_edit(request, pk):
    lab = get_object_or_404(Laboratory, pk=pk)
    
    if request.user != lab.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu laboratoriya ishini o'zgartira olmaysiz!")
        return redirect('labaratoriya_list')
    
    if request.method == 'POST':
        form = LaboratoryForm(request.POST, request.FILES, instance=lab)
        if form.is_valid():
            form.save()
            messages.success(request, "Laboratoriya ishi muvaffaqiyatli o'zgartirildi!")
            return redirect('labaratoriya_detail', pk=lab.pk)
    else:
        form = LaboratoryForm(instance=lab)
    
    return render(request, 'labaratoriya/labaratoriya_form.html', {'form': form, 'lab': lab, 'action': 'edit'})

@login_required
def labaratoriya_delete(request, pk):
    lab = get_object_or_404(Laboratory, pk=pk)
    
    if request.user != lab.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu laboratoriya ishini o'chira olmaysiz!")
        return redirect('labaratoriya_list')
    
    if request.method == 'POST':
        lab.delete()
        messages.success(request, "Laboratoriya ishi muvaffaqiyatli o'chirildi!")
        return redirect('labaratoriya_list')
    
    return render(request, 'labaratoriya/labaratoriya_confirm_delete.html', {'lab': lab})