# amaliy/forms.py
from django import forms
from .models import PracticalTask

class PracticalTaskForm(forms.ModelForm):
    class Meta:
        model = PracticalTask
        fields = ['title', 'description', 'problem_text', 'google_docs_url', 'image', 'solution']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'problem_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'google_docs_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://docs.google.com/document/d/...'
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'solution': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }