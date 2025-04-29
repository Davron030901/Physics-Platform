# simulation_games/admin.py
from django.contrib import admin
from .models import SimulationGame

@admin.register(SimulationGame)
class SimulationGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'added_by', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')