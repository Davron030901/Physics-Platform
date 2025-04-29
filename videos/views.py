# videos/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.filter(is_active=True)
    return render(request, 'videos/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk, is_active=True)
    related_videos = Video.objects.filter(is_active=True).exclude(pk=pk)[:4]
    return render(request, 'videos/video_detail.html', {
        'video': video,
        'related_videos': related_videos
    })