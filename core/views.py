"""
Session 3 — Student Management Platform (Phase 1)
core/views.py

Complete the views below. Each view should:
1. Prepare any data needed (from the STUDENTS list)
2. Return render() with the appropriate template and context
"""

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Student, Course 


ROLE_ADMIN = "Admin"
ROLE_VIEWER = "Viewer"
AVAILABLE_ROLES = (ROLE_ADMIN, ROLE_VIEWER)


def is_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


def staff_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not is_admin(request.user):
            return HttpResponseForbidden("You do not have permission to access this page.")
        return view_func(request, *args, **kwargs)

    return _wrapped_view



def home(request):
    """Home page — welcome message."""
    # TODO: render home.html
    return render(request, 'home.html')


def about(request):
    """About page — course information."""
    # TODO: render about.html
    return render(request, 'about.html')

def login_view(request):
    """Login page — form to log in."""  
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("student_list")
        else:
            error_message = "Invalid username or password."
            return render(request, "login.html", {"error_message": error_message})
    return render(request, "login.html")


def register_user(request):
    if request.user.is_authenticated:
        return redirect("student_list")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        selected_role = request.POST.get("role", "")

        if not username:
            return render(
                request,
                "register_user.html",
                {"roles": AVAILABLE_ROLES, "error_message": "Username is required."},
            )

        if password != confirm_password:
            return render(
                request,
                "register_user.html",
                {"roles": AVAILABLE_ROLES, "error_message": "Passwords do not match."},
            )

        if selected_role not in AVAILABLE_ROLES:
            return render(
                request,
                "register_user.html",
                {"roles": AVAILABLE_ROLES, "error_message": "Please select a valid role."},
            )

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "register_user.html",
                {"roles": AVAILABLE_ROLES, "error_message": "Username already exists."},
            )

        user = User.objects.create_user(username=username, password=password)
        user.is_staff = selected_role == ROLE_ADMIN
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register_user.html", {"roles": AVAILABLE_ROLES})

def logout_view(request):
    """Logout view — log the user out and redirect to home."""
    logout(request)
    return redirect("home")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated successfully.")
            return redirect("student_list")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, "change_password.html", {"form": form})

@login_required
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
        'shown_students': students.count(),
        'can_manage_students': is_admin(request.user),
    })

@login_required
def student_detail(request, student_id):
        
   student = get_object_or_404(Student, id=student_id)
   return render(request, "student_detail.html", {"student": student})


@staff_required
def add_student(request):
    if request.method == "POST":
                Student.objects.create(
                        name=request.POST.get("name"),
                        email=request.POST.get("email"),
                        course_id=request.POST.get("course"),
                        grade=request.POST.get("grade"),
            created_by=request.user.username,
                )
                return redirect("student_list")
    return render(request, "add_student.html", {"courses": Course.objects.all()}) 

@staff_required
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

@staff_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    
    return render(request, "delete_student.html", {"student": student})

@login_required
def course_list(request):
    # TODO: get all courses, render course_list.html
    courses = Course.objects.all()
    return render(
        request,
        "course_list.html",
        {
            "courses": courses,
            "students": Student.objects.all(),
            "can_edit_courses": is_admin(request.user),
        },
    )

@login_required
def course_detail(request, course_id):
    # TODO: get_object_or_404(Course, id=course_id)
    # TODO: pass course and course.students.all() to template
        course = get_object_or_404(Course, id=course_id)
        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "students": Student.objects.filter(course=course),
                "can_edit_courses": is_admin(request.user),
            },
        )

@staff_required
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == "POST":
        course.name = request.POST.get("name")
        course.description = request.POST.get("description")
        course.save()
        return redirect("course_list")
    
    return render(request, "edit_course.html", {"course": course})

