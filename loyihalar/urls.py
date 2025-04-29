# loyihalar/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loyiha_list, name='loyiha_list'),
    path('<int:pk>/', views.loyiha_detail, name='loyiha_detail'),
    path('create/', views.loyiha_create, name='loyiha_create'),
    path('<int:pk>/edit/', views.loyiha_edit, name='loyiha_edit'),
    path('<int:pk>/submit/', views.loyiha_submit, name='loyiha_submit'),
    path('<int:pk>/review/', views.loyiha_review, name='loyiha_review'),
    path('<int:pk>/delete/', views.loyiha_delete, name='loyiha_delete'),
]