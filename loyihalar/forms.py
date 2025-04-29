# loyihalar/forms.py
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ProjectReviewForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['status', 'feedback', 'grade']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'grade': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
        }