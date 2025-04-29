# amaliy/admin.py
from django.contrib import admin
from .models import PracticalTask

@admin.register(PracticalTask)
class PracticalTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'has_google_docs', 'created_at')
    list_filter = ('created_at', 'teacher')
    search_fields = ('title', 'description', 'problem_text')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'teacher')
        }),
        ('Masala mazmuni', {
            'fields': ('problem_text', 'google_docs_url', 'image', 'solution')
        }),
    )
    
    def has_google_docs(self, obj):
        return bool(obj.google_docs_url)
    has_google_docs.boolean = True
    has_google_docs.short_description = 'Google Docs'
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj and not request.user.is_superuser:
            form.base_fields['teacher'].initial = request.user
        return form