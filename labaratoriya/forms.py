# labaratoriya/forms.py
from django import forms
from .models import Laboratory

class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ['title', 'description', 'instructions', 'google_docs_url', 'simulation_url', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'google_docs_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://docs.google.com/document/d/...'
            }),
            'simulation_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://phet.colorado.edu/sims/...'
            }),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }