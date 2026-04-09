# Student Management Platform - Setup Guide

A Django-based student and course management platform.

## Prerequisites

- Python 3.11+ installed
- Git (to clone the repository)

## Installation Steps

### 1. Clone the Repository
```bash
git clone <repository-url>
cd django-mvt
```

### 2. Create a Virtual Environment
```bash
# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account) - Optional
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

## Project Structure

```
django-mvt/
├── core/                    # Main app
│   ├── models.py           # Database models (Student, Course)
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   ├── templates/          # HTML templates
│   ├── static/css/         # Stylesheets
│   └── migrations/         # Database migrations
├── studentplatform/        # Project settings
│   ├── settings.py         # Django configuration
│   ├── urls.py             # Main URL router
│   └── wsgi.py             # WSGI application
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database (local)
└── requirements.txt        # Python dependencies
```

## Features

- **Student Management**: Add, edit, view, and delete students
- **Course Management**: Create and manage courses
- **Course Enrollment**: Assign students to courses with grades
- **Search & Filter**: Filter students by course
- **Grade Tracking**: Assign and update student grades
- **Responsive UI**: Clean, card-based interface

## Available Views

- `/` — Home page
- `/about/` — About page
- `/students/` — List all students
- `/students/add/` — Add a new student
- `/students/<id>/` — View student details
- `/students/edit/<id>/` — Edit student information
- `/students/delete/<id>/` — Delete a student
- `/courses/` — List all courses
- `/courses/<id>/` — View course details with enrolled students
- `/courses/edit/<id>/` — Edit course information

## Database Models

### Student
- Name (CharField)
- Email (EmailField, unique)
- Course (ForeignKey to Course)
- Grade (CharField: A, B, C, D, F, N/A)
- Active Status (BooleanField)
- Date of Birth (DateField, optional)
- Created At (DateTimeField)

### Course
- Name (CharField)
- Code (CharField, unique)
- Description (TextField, optional)
- Students (Reverse relation via ForeignKey)

## Common Commands

```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Access Django shell (interactive)
python manage.py shell

# Create admin user
python manage.py createsuperuser

# Access admin panel at: http://127.0.0.1:8000/admin/
```

## Troubleshooting

- **Import errors?** Make sure your virtual environment is activated
- **Database errors?** Run `python manage.py migrate` to sync the database
- **Port already in use?** Run `python manage.py runserver 8001` on a different port
- **Missing courses?** Add courses in the `/courses/` section before adding students

## Notes

- The database (`db.sqlite3`) is local and not committed to git
- Settings and secrets should be stored in `.env` file (not included in git)
- Static files are served locally during development
