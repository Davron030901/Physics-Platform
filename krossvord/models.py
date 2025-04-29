# krossvord/models.py
from django.db import models
from django.contrib.auth.models import User

class WordGame(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.CharField(max_length=50, verbose_name="Javob")
    hint = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yordam")
    
    class Meta:
        verbose_name = "So'z o'yini"
        verbose_name_plural = "So'z o'yinlari"
    
    def __str__(self):
        return f"{self.question} ({self.answer})"

# Krossvord modellari
class Crossword(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Oson'),
        ('medium', 'O\'rta'),
        ('hard', 'Qiyin'),
    ], default='medium', verbose_name="Qiyinlik darajasi")
    
    class Meta:
        verbose_name = "Krossvord"
        verbose_name_plural = "Krossvordlar"
    
    def __str__(self):
        return self.title

class CrosswordClue(models.Model):
    crossword = models.ForeignKey(Crossword, on_delete=models.CASCADE, related_name='clues')
    number = models.IntegerField(verbose_name="Raqam")
    clue = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.CharField(max_length=50, verbose_name="Javob")
    # krossvord/models.py (davomi)
    row = models.IntegerField(verbose_name="Satr")
    col = models.IntegerField(verbose_name="Ustun")
    direction = models.CharField(max_length=10, choices=[
        ('across', 'Gorizontal'),
        ('down', 'Vertikal'),
    ], verbose_name="Yo'nalish")
    
    class Meta:
        verbose_name = "Krossvord savoli"
        verbose_name_plural = "Krossvord savollari"
        ordering = ['number']
    
    def __str__(self):
        return f"{self.number}. {self.clue} ({self.answer})"