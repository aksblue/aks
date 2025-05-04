# Mini Registrar System

## Overview

This project is a mini registrar system with three main modules:

- **Admin Module**
- **Student Module**
- **Instructor Module**

The system allows an admin to add students, instructors, and courses, and view information.  
Students can enroll in courses and view their enrollments.  
Instructors can see the courses they are assigned to.  
All data is saved in CSV files.

## Files

- `admin_module.py` – Manages the admin interface and allows adding students, instructors, and courses.  
- `admin_login.py` – Handles the admin login process.  
- `admins.csv` – Stores admin account information.  
- `classes.py` – Defines the classes (Student, Instructor, Course, etc.).  
- `instructors_login.py` – Handles the instructor login process.  
- `student_module.py` – Manages the student interface for course enrollment and viewing courses.  
- `utilities.py` – Contains utility functions like reading and writing CSV files.

## How to Run

1. Make sure the `admins.csv` file is in the same folder as the `.py` files.
2. Open `admins.csv` to view admin usernames and passwords.
3. To run each module:
   - **Admin:** Run `admin_login.py`
   - **Student:** Run `student_module.py`
   - **Instructor:** Run `instructors_login.py`

Each script opens its own interface for interacting with the system.
