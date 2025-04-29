# core/views.py
from django.shortcuts import render

def index(request):
    # Tizimga kirgan foydalanuvchining ma'lumotlari
    user_profile = None
    if request.user.is_authenticated:
        user_profile = request.user.profile
    
    return render(request, 'index.html', {'user_profile': user_profile})