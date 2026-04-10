from core.serializers import CourseSerializer
from core.serializers import StudentSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Course, Student


class StudentPagination(PageNumberPagination):
    page_size = 5


def apply_student_filters(queryset, query_params):
    search = query_params.get('search')
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search)
            | Q(email__icontains=search)
            | Q(course__name__icontains=search)
            | Q(course__code__icontains=search)
        )

    grade = query_params.get('grade')
    if grade:
        queryset = queryset.filter(grade=grade)

    is_active = query_params.get('is_active')
    if is_active is not None:
        normalized = is_active.strip().lower()
        if normalized in {'true', '1', 'yes'}:
            queryset = queryset.filter(is_active=True)
        elif normalized in {'false', '0', 'no'}:
            queryset = queryset.filter(is_active=False)

    return queryset

#---Course Endpoints---#
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

#---Student Endpoints---#
class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    pagination_class = StudentPagination

    def get_queryset(self):
        queryset = Student.objects.all()
        return apply_student_filters(queryset, self.request.query_params)

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#---Additional API Views---#
class CourseStudentsAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = StudentPagination

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        queryset = Student.objects.filter(course__id=course_id)
        return apply_student_filters(queryset, self.request.query_params)


