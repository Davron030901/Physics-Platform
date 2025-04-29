# simulation_games/forms.py
from django import forms
from .models import SimulationGame

class SimulationGameForm(forms.ModelForm):
    class Meta:
        model = SimulationGame
        fields = ['title', 'description', 'iframe_url', 'thumbnail', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'iframe_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://phet.colorado.edu/sims/html/...'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }