"""
file name:instructors_login.py

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
from utilities import Instructor, read_csv, login_attempts, entered,clear_terminal



# Instructor login function for instructor
def instructor_login():
    instructor = login_attempts(Instructor, "instructors.csv")
    if instructor:  # If login is successful
        clear_terminal()  # Clear the screen
        entered(types='*', count=20, suffix='^', message="Login Successful!", final='yes')
        instructor_dashboard(instructor)  # Pass the instructor object to the dashboard


########################################################################
# Instructor dashboard function
def instructor_dashboard(instructor):
    time.sleep(1)
    clear_terminal()
    while True:
        clear_terminal()  # Clear the screen after each dashboard display
        entered(types='_', count=30, suffix='+', message='Welcome, ' + instructor.first_name + ' What would you like to do?', final='yes')
        print("| a. See all courses assigned to you | b. Logout                    |")
        entered(types='-', count=30, suffix='+', message="", final='no')

        entered(types='_', count=30, suffix='|', message="Please select an option", final='yes')
        choice = input("Option (a-b): ").strip().lower()  #  clean user  input

        if choice == "a":
            clear_terminal()  # Clear screen before showing courses
            see_all_courses(instructor)
        elif choice == "b":
            entered(types='-', count=30, suffix='-', message="Logging out", final='yes')
            break
        else:
            entered('~', 10, suffix='>', message='Please choose between "a" or "b".', final='yes')
            time.sleep(2)  # Pause for 2 seconds before continuing







###################################################################

# See all courses assigned to the instructor
def see_all_courses(instructor):
    entered(types='*', count=20, suffix='^', message="Courses Assigned to You", final='yes')
    courses = read_csv("courses.csv")

    assigned_courses = [course for course in courses if course['instructor_username'] == instructor.username]  # Filter based on instructor's username

    if not assigned_courses:
        entered(types='-', count=20, suffix='-', message="No courses assigned yet", final='yes')
        time.sleep(2)
    else:
        header = "{:<15} {:<25} {:<20}".format('Course Number', 'Title', 'Instructor Username')
        separator = "-" * 60
        print(header)
        print(separator)

        for course in assigned_courses:
            course_info = "{:<15} {:<25} {:<20}".format(course['course_number'], course['title'], course['instructor_username'])
            print(course_info)

        print(separator)

    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            clear_terminal()
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')


instructor_login()
