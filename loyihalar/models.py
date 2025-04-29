# loyihalar/models.py
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Qoralama'),
        ('submitted', 'Topshirilgan'),
        ('reviewed', 'Ko\'rib chiqilgan'),
        ('approved', 'Tasdiqlangan'),
        ('rejected', 'Rad etilgan'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    file = models.FileField(upload_to='projects/', verbose_name="Fayl")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_projects', verbose_name="Talaba")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_projects', null=True, blank=True, verbose_name="O'qituvchi")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name="Holat")
    feedback = models.TextField(blank=True, null=True, verbose_name="Fikr-mulohaza")
    grade = models.IntegerField(blank=True, null=True, verbose_name="Baho")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.student.username})"