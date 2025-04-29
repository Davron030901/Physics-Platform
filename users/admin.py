# users/admin.py
from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'full_name')