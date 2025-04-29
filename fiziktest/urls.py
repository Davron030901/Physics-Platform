# fiziktest/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_list, name='test_list'),
    path('start/', views.start_test, name='start_test'),
    path('start/<str:topic>/', views.start_test, name='start_topic_test'),
    path('session/<int:session_id>/question/<int:question_index>/', views.question, name='question'),
    path('session/<int:session_id>/result/', views.test_result, name='test_result'),
]