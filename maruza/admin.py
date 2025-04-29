# maruza/admin.py
from django.contrib import admin
from .models import Lecture

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'has_file', 'has_google_docs', 'has_video', 'created_at')
    list_filter = ('created_at', 'teacher')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'
    
    def has_file(self, obj):
        return bool(obj.file)
    has_file.boolean = True
    has_file.short_description = 'Fayl'
    
    def has_google_docs(self, obj):
        return bool(obj.google_docs_url)
    has_google_docs.boolean = True
    has_google_docs.short_description = 'Google Docs'
    
    def has_video(self, obj):
        return bool(obj.video_url)
    has_video.boolean = True
    has_video.short_description = 'Video'