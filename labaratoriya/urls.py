# labaratoriya/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.labaratoriya_list, name='labaratoriya_list'),
    path('<int:pk>/', views.labaratoriya_detail, name='labaratoriya_detail'),
    path('create/', views.labaratoriya_create, name='labaratoriya_create'),
    path('<int:pk>/edit/', views.labaratoriya_edit, name='labaratoriya_edit'),
    path('<int:pk>/delete/', views.labaratoriya_delete, name='labaratoriya_delete'),
]