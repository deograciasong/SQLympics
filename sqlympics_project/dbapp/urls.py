from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student_login/', views.student_login),
    path('student_dashboard/', views.student_dashboard),
    path('instructor_login/', views.instructor_login),
    path('instructor_dashboard/', views.instructor_dashboard),
    path('register/', views.register),
    path('chatbot/', views.chatbot, name='chatbot'),
]