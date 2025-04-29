# amaliy/models.py
from django.db import models
from django.contrib.auth.models import User

class PracticalTask(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    problem_text = models.TextField(verbose_name="Masala matni")
    google_docs_url = models.URLField(blank=True, null=True, verbose_name="Google Docs havolasi")
    image = models.ImageField(upload_to='practical_tasks/', blank=True, null=True, verbose_name="Rasm")
    solution = models.TextField(blank=True, null=True, verbose_name="Yechim")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='practical_tasks', verbose_name="O'qituvchi")

    class Meta:
        verbose_name = "Amaliy mashg'ulot"
        verbose_name_plural = "Amaliy mashg'ulotlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
        
    def get_display_url(self):
        if self.google_docs_url:
            return self.google_docs_url
        return None