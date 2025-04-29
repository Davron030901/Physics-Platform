# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.student_portfolio, name='student_portfolio'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]