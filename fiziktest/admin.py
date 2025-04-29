# fiziktest/admin.py
from django.contrib import admin
from .models import Question, Choice, UserAnswer, TestSession

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'time_limit', 'points')
    list_filter = ('topic', 'time_limit')
    search_fields = ('text',)
    inlines = [ChoiceInline]
    
    def save_model(self, request, obj, form, change):
        # O'qituvchi avtomatik ravishda savol egasi bo'ladi
        if not change:  # Yangi savol yaratilganda
            obj.teacher = request.user
        super().save_model(request, obj, form, change)

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'choice', 'is_correct', 'submitted_at')
    list_filter = ('is_correct', 'submitted_at')
    search_fields = ('user__username',)

@admin.register(TestSession)
class TestSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'total_questions', 'started_at', 'finished_at')
    list_filter = ('started_at',)
    search_fields = ('user__username',)