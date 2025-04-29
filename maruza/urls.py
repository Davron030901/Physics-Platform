# maruza/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.maruza_list, name='maruza_list'),
    path('<int:pk>/', views.maruza_detail, name='maruza_detail'),
    path('create/', views.maruza_create, name='maruza_create'),
    path('<int:pk>/edit/', views.maruza_edit, name='maruza_edit'),
    path('<int:pk>/delete/', views.maruza_delete, name='maruza_delete'),
]