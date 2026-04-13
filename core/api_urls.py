from django.urls import path
from .api_views import CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, CourseStudentsAPIView 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    #---Course API Endpoints---#
    path('courses/', CourseListCreateAPIView.as_view(), name='api_course_list_create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='api_course_detail'),
    #---Student API Endpoints---#
    path('students/', StudentListCreateAPIView.as_view(), name='api_student_list_create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='api_student_detail'),
    #---All students in a course---#
    path('courses/<int:course_id>/students/', CourseStudentsAPIView.as_view(), name='api_course_students'),

    #---JWT Authentication Endpoints---#
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]