from django.contrib import admin
from .models import Student, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "name"]
    search_fields = ["name", "code"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "course", "grade", "is_active"]
    list_filter = ["course", "grade", "is_active"]
    search_fields = ["name", "email"]
    list_per_page = 20

# Register your models here.
