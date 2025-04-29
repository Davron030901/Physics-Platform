# amaliy/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.amaliy_list, name='amaliy_list'),
    path('<int:pk>/', views.amaliy_detail, name='amaliy_detail'),
    path('create/', views.amaliy_create, name='amaliy_create'),
    path('<int:pk>/edit/', views.amaliy_edit, name='amaliy_edit'),
    path('<int:pk>/delete/', views.amaliy_delete, name='amaliy_delete'),
]