# sonmetodi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.multiplication_game, name='multiplication_game'),
]