# maruza/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Lecture
from .forms import LectureForm

def maruza_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'maruza/maruza_list.html', {'lectures': lectures})

# maruza/views.py (maruza_detail funksiyasi yangilangan)
def maruza_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    
    # Oldingi va keyingi ma'ruzalarni topish
    prev_lecture = Lecture.objects.filter(created_at__lt=lecture.created_at).order_by('-created_at').first()
    next_lecture = Lecture.objects.filter(created_at__gt=lecture.created_at).order_by('created_at').first()
    
    return render(request, 'maruza/maruza_detail.html', {
        'lecture': lecture,
        'prev_lecture': prev_lecture,
        'next_lecture': next_lecture
    })
@login_required
def maruza_create(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.teacher = request.user
            lecture.save()
            messages.success(request, "Ma'ruza muvaffaqiyatli qo'shildi!")
            return redirect('maruza_list')
    else:
        form = LectureForm()
    
    return render(request, 'maruza/maruza_form.html', {'form': form, 'action': 'create'})

@login_required
def maruza_edit(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    
    if request.user != lecture.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu ma'ruzani o'zgartira olmaysiz!")
        return redirect('maruza_list')
    
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'ruza muvaffaqiyatli o'zgartirildi!")
            return redirect('maruza_detail', pk=lecture.pk)
    else:
        form = LectureForm(instance=lecture)
    
    # maruza/views.py (davomi)
    return render(request, 'maruza/maruza_form.html', {'form': form, 'lecture': lecture, 'action': 'edit'})

@login_required
def maruza_delete(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    
    if request.user != lecture.teacher and not request.user.is_staff:
        messages.error(request, "Siz bu ma'ruzani o'chira olmaysiz!")
        return redirect('maruza_list')
    
    if request.method == 'POST':
        lecture.delete()
        messages.success(request, "Ma'ruza muvaffaqiyatli o'chirildi!")
        return redirect('maruza_list')
    
    return render(request, 'maruza/maruza_confirm_delete.html', {'lecture': lecture})