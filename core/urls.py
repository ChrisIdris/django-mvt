"""
Session 3 — Student Management Platform (Phase 1)
core/urls.py

Define URL patterns for the core app.
Each path maps a URL to a view function.
"""

from django.urls import path
from . import views

urlpatterns = [
    # TODO: add paths for home, about, student_list, student_detail, add_student
    # Example: path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/edit/<int:course_id>/', views.edit_course, name='edit_course'),
]