# users/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

def student_portfolio(request):
    students = Profile.objects.filter(role='student')
    return render(request, 'users/student_portfolio.html', {'students': students})

@login_required
def profile_view(request):
    """Foydalanuvchi profili ko'rinishi"""
    profile = request.user.profile
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    """Foydalanuvchi profilini tahrirlash"""
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profilingiz muvaffaqiyatli yangilandi!")
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'users/profile_edit.html', {'form': form})