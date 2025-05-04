"""
file name:student_module.p


Problem Description:

Mini Registrar System
A simple system with Admin, Student, and Instructor modules.
Admin can add students, instructors, and courses, and view data.
Students can enroll in courses and view their enrollments.
Instructors can see the courses they teach. Data is stored in CSV files.

Variables:
"student"                   To represent the student object throughout this module.
"student_data"              To store the student's
"student_username"          To store the student's username
"entered"                   To print formatted messages and symbols
"choice"                    To store the student's menu choice
"enrollments"               To store the list of enrollments for the courses
"enrolled_courses"          To store the student's enrolled courses
"header"                    column headers to display the courses
"separator"                 separator line for course display
"enrollment_info"           To store information about the student's course enrollment
"selection"                 To store the student's for going back to the main menu
"courses"                   To store available courses for enrollment
"course_index"              To display the numbers for each course
"course_choice"             To store the selected course number
"selected_course"           To store the data of the course chosen for enrollment
"course_number"             To store the course number of the selected course
"enrollment"                New object when the student enrolls in a course
"Enrollment"                An object type used to store enrollment data
"write_csv"                 To write the new enrollment data to the file


First Create Date: Nov21, 2024
Last Update Date: dec 10, 2024
Author: aksblue
Version: 1.0
"""

import time
from utilities import Student, read_csv, write_csv, login_attempts, Enrollment, entered,clear_terminal



# Student login function
def student_login():
    clear_terminal()  # Clear the screen before login
    student = login_attempts(Student, "students.csv")
    if student:
        entered(types='*', count=20, suffix='^', message="Login Successful!", final='yes')
        time.sleep(1)
        student_dashboard(student)  # pass the student object to the dashboard if the login is successful
    else:
        entered(types='-', count=20, suffix='-', message="Login failed. Please try again.", final='yes')


############################################################################





#the studnets main menu
def student_dashboard(student):
    while True:
        clear_terminal()  # Clear the screen after each dashboard display
        entered(types='=', count=30, suffix='+', message='Welcome, ' + student.first_name + ' What would you like to do?', final='yes')
        print("| a. View enrolled courses   | b. Enroll in a new course   |")
        print("| c. Logout                  |")
        entered(types='=', count=30, suffix='+', message="", final='no')

        entered(types='-', count=30, suffix='-', message="Please select an option", final='yes')
        choice = input("Option (a-c): ").strip().lower()  # to Clean the input

        if choice == "a":
            clear_terminal()  # clears the screen before showing enrolled courses
            see_enrolled_courses(student)
        elif choice == "b":
            clear_terminal()
            enroll_in_course(student)
        elif choice == "c":
            entered(types='-', count=30, suffix='-', message="Logging out", final='yes')
            break
        else:
            entered('~', 10, suffix='>', message='Please try again.', final='yes')
            time.sleep(2)  # Pause for a 2 seconds before continuing






############################################################################


#functions to see enrolled course
def see_enrolled_courses(student):
    entered(types='*', count=20, suffix='^', message="Enrolled Courses", final='yes')
    enrollments = read_csv("enrollments.csv")

    enrolled_courses = [enrollment for enrollment in enrollments if enrollment['student_username'] == student.username]

    if not enrolled_courses:
        entered(types='-', count=20, suffix='-', message="No courses enrolled yet", final='yes')
    else:
        header = "{:<15} {:<15}".format('Student Username', 'Course Number')
        separator = "-" * 40
        print(header)
        print(separator)

        for enrollment in enrolled_courses:
            enrollment_info = "{:<15} {:<15}".format(enrollment['student_username'], enrollment['course_number'])
            print(enrollment_info)

        print(separator)

    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')






#######################################################################3



#funtions to show the course student is enroll in

def enroll_in_course(student):
    entered(types='*', count=20, suffix='^', message="Available Courses", final='yes')
    courses = read_csv("courses.csv")

    # Display courses with corresponding numbers
    if not courses:
        entered(types='-', count=20, suffix='-', message="No courses available.", final='yes')
        return

    header = "{:<5} {:<15} {:<25} {:<20}".format('No.', 'Course Number', 'Title', 'Instructor')
    separator = "-" * 60
    print(header)
    print(separator)

    course_index = 1
    for course_data in courses:
        course_info = "{:<5} {:<15} {:<25} {:<20}".format(course_index, course_data['course_number'], course_data['title'], course_data['instructor_username'])
        print(course_info)
        course_index += 1

    print(separator)

    # Prompt the user to select a course by number
    try:
        course_choice = int(input("Enter the corresponding number of the course you want to enroll in: "))

        # chekcs the selected number
        if course_choice < 1 or course_choice > len(courses):
            entered(types='-', count=20, suffix='-', message="Please try again.", final='yes')
            return

        selected_course = courses[course_choice - 1]
        course_number = selected_course['course_number']  # Get the course number from the selected course

        # Check if the student is already enrolled in the course
        enrollments = read_csv("enrollments.csv")
        for enrollment in enrollments:
            if enrollment['student_username'] == student.username and enrollment['course_number'] == course_number:
                entered(types='-', count=20, suffix='-', message="You are already enrolled in this course.", final='yes')
                return

        # Enroll the student in the course selected
        enrollment = Enrollment(student.username, course_number)
        write_csv("enrollments.csv", enrollment)
        entered(types='-', count=20, suffix='-', message="Enrollment in " + selected_course['title'] + " successful.", final='yes')

    except:
        entered(types='-', count=20, suffix='-', message="Please enter a number.", final='yes')



student_login()  # Call the login function to start the process
