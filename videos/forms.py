# videos/forms.py
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_url', 'thumbnail', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://www.youtube.com/watch?v=VIDEO_ID'
            }),            
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'video_url': 'YouTube video havolasini kiriting (masalan: https://www.youtube.com/watch?v=pmFgJEB-AZ0). Havola avtomatik ravishda joylashtirish formatiga o\'zgartiriladi.'
        }