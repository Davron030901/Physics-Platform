# simulation_games/models.py
from django.db import models
from django.contrib.auth.models import User

class SimulationGame(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    iframe_url = models.URLField(verbose_name="Simulyatsiya URL manzili")
    thumbnail = models.ImageField(upload_to='simulation_games/', blank=True, null=True, verbose_name="Oldindan ko'rinish tasviri")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simulation_games', verbose_name="Qo'shgan foydalanuvchi")
    
    class Meta:
        verbose_name = "Simulyatsion o'yin"
        verbose_name_plural = "Simulyatsion o'yinlar"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title