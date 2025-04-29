# krossvord/admin.py
from django.contrib import admin
from .models import WordGame, Crossword, CrosswordClue

class CrosswordClueInline(admin.TabularInline):
    model = CrosswordClue
    extra = 1

@admin.register(WordGame)
class WordGameAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'hint')
    search_fields = ('question', 'answer')

@admin.register(Crossword)
class CrosswordAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'get_clue_count')
    list_filter = ('difficulty',)
    search_fields = ('title', 'description')
    inlines = [CrosswordClueInline]
    
    def get_clue_count(self, obj):
        return obj.clues.count()
    get_clue_count.short_description = 'Savollar soni'