"""
Session 3 — Student Management Platform (Phase 1)
core/views.py

Complete the views below. Each view should:
1. Prepare any data needed (from the STUDENTS list)
2. Return render() with the appropriate template and context
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course 



def home(request):
    """Home page — welcome message."""
    # TODO: render home.html
    return render(request, 'home.html')


def about(request):
    """About page — course information."""
    # TODO: render about.html
    return render(request, 'about.html')


def student_list(request):
    """List all students in a table."""
    all_students = Student.objects.all()
    students = all_students
    
    # Handle search by name
    search_query = request.GET.get('search')
    if search_query:
        students = students.filter(name__icontains=search_query)
    
    # Handle course filtering
    course_filter = request.GET.get('course')
    if course_filter:
        students = students.filter(course__code=course_filter)
    
    # TODO: pass STUDENTS and the total count to student_list.html
    return render(request, 'student_list.html', {
        'students': students, 
        'courses': Course.objects.all(),
        'search': search_query or '',
        'selected_course': course_filter or '',
        'total_students': all_students.count(),
        'shown_students': students.count()
    })


def student_detail(request, student_id):
        
   student = get_object_or_404(Student, id=student_id)
   return render(request, "student_detail.html", {"student": student})


from django.shortcuts import render, redirect

def add_student(request):
    if request.method == "POST":
      Student.objects.create(
        name=request.POST.get("name"),
        email=request.POST.get("email"),
        course_id=request.POST.get("course"),
        grade=request.POST.get("grade"),
      )
    return render(request, "add_student.html", {"courses": Course.objects.all()}) 

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        course_code = request.POST.get("course")
        student.course = Course.objects.get(code=course_code)
        student.grade = request.POST.get("grade")
        student.save()
        return redirect("student_list")
    
    return render(request, "edit_student.html", {"student": student, "courses": Course.objects.all()})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    
    return render(request, "delete_student.html", {"student": student})

def course_list(request):
    # TODO: get all courses, render course_list.html
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses, "students": Student.objects.all()})


def course_detail(request, course_id):
    # TODO: get_object_or_404(Course, id=course_id)
    # TODO: pass course and course.students.all() to template
        course = get_object_or_404(Course, id=course_id)
        return render(request, "course_detail.html", {"course": course, "students": Student.objects.filter(course=course)})

def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == "POST":
        course.name = request.POST.get("name")
        course.description = request.POST.get("description")
        course.save()
        return redirect("course_list")
    
    return render(request, "edit_course.html", {"course": course})

