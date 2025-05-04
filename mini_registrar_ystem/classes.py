"""
file name: classes.py



Problem Description:

Mini Registrar System
A simple system with Admin, Student, and Instructor modules.
Admin can add students, instructors, and courses, and view data.
Students can enroll in courses and view their enrollments.
Instructors can see the courses they teach. Data is stored in CSV files.


First Create Date: Nov21, 2024
Last Update Date: dec 10, 2024
Author: aksblue
Version: 1.0
"""

# Parent class for all users (Admin, Student, Instructor)
class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name  # First name of the user
        self.last_name = last_name    # Last name of the user
        self.username = username      # Username of the user
        self.password = password      # Password of the user


    def get_first_name(self):
        return self.first_name

# Class to represent an enrollment (student enrolling in a course)
class Enrollment:
    def __init__(self, student_username, course_number):
        self.student_username = student_username  # Student's username
        self.course_number = course_number        # Course number the student is enrolled in


# Class to represent a course
class Course:
    def __init__(self, course_number, title, instructor):
        self.course_number = course_number        # Unique course number
        self.title = title                        # Title of the course
        self.instructor = instructor  # Instructor's username for this course



# Class for Student which inherits from User
class Student(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)  # Inherit from User class

# Class for Instructor which inherits from User
class Instructor(User):
    def __init__(self, first_name, last_name, username, password, title):
        super().__init__(first_name, last_name, username, password)  # Inherit from User class
        self.title = title  # Title of the instructor (e.g., Assistant Professor, Professor)


    def get_title(self):
        return self.title
