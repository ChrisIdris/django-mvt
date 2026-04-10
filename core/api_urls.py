from django.urls import path
from .api_views import CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, CourseStudentsAPIView 


urlpatterns = [
    #---Course API Endpoints---#
    path('courses/', CourseListCreateAPIView.as_view(), name='api_course_list_create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='api_course_detail'),
    #---Student API Endpoints---#
    path('students/', StudentListCreateAPIView.as_view(), name='api_student_list_create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='api_student_detail'),
    #---All students in a course---#
    path('courses/<int:course_id>/students/', CourseStudentsAPIView.as_view(), name='api_course_students'),
]