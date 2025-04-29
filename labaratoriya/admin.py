# labaratoriya/admin.py
from django.contrib import admin
from .models import Laboratory

@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'has_google_docs', 'has_simulation', 'created_at')
    list_filter = ('created_at', 'teacher')
    search_fields = ('title', 'description', 'instructions')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'teacher')
        }),
        ('Laboratoriya mazmuni', {
            'fields': ('instructions', 'google_docs_url', 'simulation_url', 'file')
        }),
    )
    
    def has_google_docs(self, obj):
        return bool(obj.google_docs_url)
    has_google_docs.boolean = True
    has_google_docs.short_description = 'Google Docs'
    
    def has_simulation(self, obj):
        return bool(obj.simulation_url)
    has_simulation.boolean = True
    has_simulation.short_description = 'Simulyatsiya'
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj and not request.user.is_superuser:
            form.base_fields['teacher'].initial = request.user
        return form