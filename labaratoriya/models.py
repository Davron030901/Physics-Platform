# labaratoriya/models.py
from django.db import models
from django.contrib.auth.models import User

class Laboratory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    instructions = models.TextField(verbose_name="Ko'rsatmalar")
    google_docs_url = models.URLField(blank=True, null=True, verbose_name="Google Docs havolasi")
    simulation_url = models.URLField(blank=True, null=True, verbose_name="Simulyatsiya havolasi")
    file = models.FileField(upload_to='laboratory/', blank=True, null=True, verbose_name="Fayl")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='laboratories', verbose_name="O'qituvchi")

    class Meta:
        verbose_name = "Laboratoriya ishi"
        verbose_name_plural = "Laboratoriya ishlari"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
        
    def get_display_url(self):
        if self.google_docs_url:
            return self.google_docs_url
        return None