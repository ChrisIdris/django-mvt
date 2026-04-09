from django.db import models

class Course(models.Model):
    """A course that students can enrol in."""

    # TODO: add fields
    # name — CharField, max_length=100
    # code — CharField, max_length=10, unique=True
    # description — TextField, blank=True
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True) 
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} — {self.name}"


class Student(models.Model):
    """A student enrolled in a course."""

    # TODO: add fields
    # name — CharField, max_length=100
    # email — EmailField, unique=True
    # date_of_birth — DateField, null=True, blank=True
    # grade — CharField, max_length=2, default="N/A"
    # is_active — BooleanField, default=True
    # course — ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    # created_at — DateTimeField, auto_now_add=True
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=2, default="N/A")
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students", default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
