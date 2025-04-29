# suzmetodi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.suz_game, name='suz_game'),
]