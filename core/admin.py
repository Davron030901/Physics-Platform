# core/admin.py fayli
from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Admin paneliga sarlavha va sarlavha ostini o'zgartirish
admin.site.site_header = 'Fizika Ta\'lim Platformasi'
admin.site.site_title = 'Fizika admin'
admin.site.index_title = 'Boshqaruv paneli'

# Log yozuvlarini ko'rsatish (ma'murlar uchun)
@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('action_time', 'user', 'content_type', 'object_repr', 'action_flag')
    list_filter = ('action_time', 'user', 'content_type')
    search_fields = ('object_repr', 'change_message')
    date_hierarchy = 'action_time'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False