# fiziktest/models.py
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    TOPICS = [
        ('kinematika', 'Kinematika'),
        ('dinamika', 'Dinamika'),
        ('ish_va_energiya', 'Ish va Energiya'),
        ('impuls', 'Impuls'),
        ('gravitatsiya', 'Gravitatsiya'),
    ]
    
    topic = models.CharField(max_length=50, choices=TOPICS, verbose_name="Mavzu")
    text = models.TextField(verbose_name="Savol")
    time_limit = models.IntegerField(default=30, verbose_name="Vaqt chegarasi (sekund)")
    points = models.IntegerField(default=1, verbose_name="Ball")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Test savoli"
        verbose_name_plural = "Test savollari"
    
    def __str__(self):
        return f"{self.topic}: {self.text[:50]}..."

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices', verbose_name="Savol")
    text = models.CharField(max_length=255, verbose_name="Variant")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri javob")
    
    class Meta:
        verbose_name = "Javob varianti"
        verbose_name_plural = "Javob variantlari"
    
    def __str__(self):
        return f"{self.text} ({'To`g`ri' if self.is_correct else 'Noto`g`ri'})"

class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_answers', verbose_name="Foydalanuvchi")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Savol")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name="Tanlangan javob")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri javob")
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Foydalanuvchi javobi"
        verbose_name_plural = "Foydalanuvchi javoblari"
        unique_together = ['user', 'question']
    
    def __str__(self):
        return f"{self.user.username}: {self.question.text[:30]}... - {self.choice.text}"

# fiziktest/models.py
class TestSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_sessions', verbose_name="Foydalanuvchi")
    score = models.IntegerField(default=0, verbose_name="Ball")
    total_questions = models.IntegerField(default=0, verbose_name="Savollar soni")
    # Qo'shish kerak bo'lgan field
    questions = models.ManyToManyField(Question, blank=True, related_name='sessions', verbose_name="Savollar")
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    
    # ... qolgan kod ...
    
    class Meta:
        verbose_name = "Test sessiyasi"
        verbose_name_plural = "Test sessiyalari"
    
    def __str__(self):
        return f"{self.user.username}: {self.score}/{self.total_questions} - {self.started_at}"