"""
file name: admin_login.py


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





import time
from utilities import login_attempts, entered, clear_terminal
from admin_module import Admin, view_students


# Admin login function to authenticate admin user
def admin_login():
    admin = login_attempts(Admin, "admins.csv")
    if admin:  # If login is successful
        clear_terminal()
        entered(types='*', count=20, suffix='^', message="Login Successful!", final='yes')
        admin_dashboard(admin)  # Pass the admin object to the dashboard






# Design for Admin Dashboard

def admin_dashboard(admin):
    time.sleep(1)
    clear_terminal()
    while True:
        entered(types='=', count=30, suffix='+', message='Welcome, ' + admin.get_first_name() +' What would you like to do?', final='yes')
        print("| a. Add a new student   | b. Add an instructor  |")
        print("| c. Add a course        | d. See all students   |")
        print("| e. See all instructors | f. See all courses    |")
        print("| h. Logout              | g. See all enrollments|")
        entered(types='=', count=30, suffix='+', message="", final='no')

        entered(types='-', count=30, suffix='-', message="Please select an option", final='yes')
        choice = input("Option (a-h): ")

        if choice == "a":
            clear_terminal()
            admin.add_student()  # the admin object's method to add a student
        elif choice == "b":
            clear_terminal()
            admin.add_instructor()  # the admin object's method to add an instructor
        elif choice == "c":
            clear_terminal()
            admin.add_course()  # the admin object's method to add a course
        elif choice == "d":
            clear_terminal()
            view_students()  # the admin object's method to view students
        elif choice == "e":
            clear_terminal()
            admin.view_instructors()  #the admin object's method to view instructors
        elif choice == "f":
            clear_terminal()
            admin.view_courses()  # the admin object's method to view courses
        elif choice == "g":
            clear_terminal()
            admin.view_enrollments()  # the admin object's method to view enrollments
        elif choice == "h":
            print("Logging out...")
            break
        else:
            entered(types='~', count=20, suffix='>', message="Please select an option between a and h to continue", final='yes')
            time.sleep(4)
            clear_terminal()
            print('\n')

admin_login()
