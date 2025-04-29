# videos/models.py
from django.db import models
from django.contrib.auth.models import User
import re

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    video_url = models.URLField(verbose_name="Video havolasi")
    thumbnail = models.ImageField(upload_to='videos/', blank=True, null=True, verbose_name="Oldindan ko'rinish")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', verbose_name="Qo'shgan foydalanuvchi")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    
    class Meta:
        verbose_name = "Qiziqarli video"
        verbose_name_plural = "Qiziqarli videolar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
        
    def get_embedded_url(self):
        """YouTube havolasini embed formatiga o'zgartirish"""
        url = self.video_url
        # YouTube havolasini embed formatiga o'zgartirish
        youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        match = re.match(youtube_regex, url)
        
        if match:
            video_id = match.group(6)
            return f'https://www.youtube.com/embed/{video_id}'
        
        # Agar boshqa formatdagi havola bo'lsa, o'zgarishsiz qaytarish
        return url