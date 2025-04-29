# fiziktest/templatetags/fiziktest_extras.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Lug'atdan kalit bo'yicha qiymatni olish uchun filter"""
    return dictionary.get(key)

@register.filter
def multiply(value, arg):
    """Ikkita sonni ko'paytirish"""
    return float(value) * float(arg)

@register.filter
def divide(value, arg):
    """Birinchi sonni ikkinchisiga bo'lish"""
    return float(value) / float(arg) if float(arg) != 0 else 0