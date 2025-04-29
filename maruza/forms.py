# maruza/forms.py
from django import forms
from .models import Lecture
import re

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'description', 'file', 'google_docs_url', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'google_docs_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://docs.google.com/document/d/...'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://www.youtube.com/watch?v=...'
            }),
        }
    
    def clean_video_url(self):
        """YouTube havolasini tekshirish"""
        video_url = self.cleaned_data.get('video_url')
        if not video_url:
            return video_url
            
        # YouTube havolasini tekshirish
        youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        match = re.match(youtube_regex, video_url)
        
        if match:
            # URL to'g'ri formatda
            return video_url
        else:
            # Agar YouTube havolasi bo'lmasa, lekin boshqa URL bo'lsa
            if video_url.startswith('http'):
                return video_url
                
            # Noto'g'ri format
            raise forms.ValidationError('Yaroqli YouTube havolasini kiriting')