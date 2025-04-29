# maruza/models.py
from django.db import models
from django.contrib.auth.models import User
import re
class Lecture(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    file = models.FileField(upload_to='lectures/', blank=True, null=True, verbose_name="Fayl")
    google_docs_url = models.URLField(blank=True, null=True, verbose_name="Google Docs havolasi")
    video_url = models.URLField(blank=True, null=True, verbose_name="Video havolasi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lectures', verbose_name="O'qituvchi")

    class Meta:
        verbose_name = "Ma'ruza"
        verbose_name_plural = "Ma'ruzalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_file_type(self):
        if self.file:
            ext = self.file.name.split('.')[-1].lower()
            if ext in ['pdf']:
                return 'pdf'
            elif ext in ['doc', 'docx']:
                return 'word'
            elif ext in ['ppt', 'pptx']:
                return 'powerpoint'
            elif ext in ['jpg', 'jpeg', 'png', 'gif']:
                return 'image'
        return 'file'
    
    def get_display_url(self):
        if self.google_docs_url:
            # Google Docs URL ni qaytarish
            return self.google_docs_url
        elif self.file:
            # Fayl URL ni qaytarish
            return self.file.url
        return None
    def get_embedded_video_url(self):
        """YouTube havolasini iframe uchun embed URL ga o'zgartirish"""
        if not self.video_url:
            return None
            
        # YouTube video ID ni olish
        youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        match = re.match(youtube_regex, self.video_url)
        
        if match:
            video_id = match.group(6)
            return f'https://www.youtube.com/embed/{video_id}'
        
        return self.video_url