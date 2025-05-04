"""
file name:admin_module.py

Problem Description:

Mini Registrar System
A simple system with Admin, Student, and Instructor modules.
Admin can add students, instructors, and courses, and view data.
Students can enroll in courses and view their enrollments.
Instructors can see the courses they teach. Data is stored in CSV files.

"first_name"             To store the student's first name
"last_name"              To store the student's last name
"username"               To store the student's username
"password"               To store the student's password
"student_data"           To store student information
"unique_username"        To make sure the username is unique
"existing_usernames"     To store existing usernames for to comapare
"new_student"            To represent a new student object being created
"file_name"              which the file to open or save to
"students_file"          To represent the file storing students
"existing_students"      To store the list of existing students
"students"               To store all students

First Create Date: Nov21, 2024
Last Update Date: dec 10, 2024
Author: aksblue
Version: 1.0
"""


from classes import Student, Instructor, Course,  User
import time
from utilities import  write_csv, is_unique_username, is_unique_password, read_csv,clear_terminal, entered


class Admin(User):
    def __init__(self, first_name, last_name, username, password):
         # Calls the parent class (User) constructor
        super().__init__(first_name, last_name, username, password)



        #to add students
    def add_student(self):
        entered(types='-', count=10, message=" Add a New Student ", final='yes') # visual text and symbols
        first_name = input("Enter student first name: ")
        entered(types='-', count=10, final='no')

        last_name = input("Enter student last name: ")
        entered(types='-', count=10, final='no')
        #ask for username and checks if its unique or ask agin if its not
        while True:
            username = input("Enter student username: ")
            entered(types='-', count=10, final='no')

            if is_unique_username('students.csv', username):
                break
            else:
                entered(types='~', count=15, suffix='>', message="Username already exists. Try another.", final='yes')#visual if username already exits
        #ask for paswords and checks if its unique or ask agin if its not
        while True:
            password = input("Enter student password: ")
            entered(types='-', count=10, final='no')
            if is_unique_password('students.csv', password):
                break
            else:
                entered(types='~', count=15, suffix='>', message='password already exists. Try another.', final='yes') #visual if password already exits

        #saves the info to the file
        student = Student(first_name, last_name, username, password)
        write_csv("students.csv", student)
        entered(types='*', count=20, suffix='^', message='Student added successfully', final='yes')
        time.sleep(2)
        clear_terminal()


    def add_instructor(self):
        # Display a border with the title
        entered(types='*', count=10, message="Add New Instructor", final='yes')

        first_name = input("Enter instructor first name: ")
        entered(types='-', count=10, final='no')
        last_name = input("Enter instructor last name: ")
        entered(types='-', count=10, final='no')

        # valid titles
        valid_titles = ["assistant professor", "associate professor", "professor"]

        # Ensure unique username
        while True:
            username = input("Enter instructor username: ")
            entered(types='-', count=10, final='no')
            if is_unique_username("instructors.csv", username):
                break
            else:
                entered(types='~', count=15, suffix='>', message='Username already exists. Try another.', final='yes')

        password = input("Enter instructor password: ")

        # Ensure valid title selection
        while True:

            entered(types='_', count=10, message="Choose a title: Assistant Professor, Associate Professor, or Professor.", final='yes')  # Display a bordered message for title input
            title = input("Enter title : ").strip().lower()
            entered(types='-', count=10, final='no')
            if title in valid_titles:
                break
            else:
                entered(types='~', count=15, suffix='>', message='Please enter one of the 5 titles.', final='yes')

        # Creates the instructor object and saves it
        instructor = Instructor(first_name, last_name, username, password, title)

        # to write the instructor data to the CSV file
        write_csv("instructors.csv", instructor)

        entered(types='*', count=10, message="Instructor added successfully.", final='yes')
        time.sleep(2)

        #to add course
    def add_course(self):
        # Display a border with a title
        entered(types='*', count=10, message="Add New Course", final='yes')

        # Course number input with validation for uniqueness
        while True:
            course_number = input("Enter course number: ")
            entered(types='-', count=10, final='no')
            if check_unique_course_number("courses.csv", course_number):
                break
            else:
                entered(types='~', count=15, suffix='>', message='Course number already exists. Try another.', final='yes')#visuals to warn


        # course title input
        title = input("Enter course title: ")
        entered(types='-', count=10, final='no')

        # Instructor username input
        while True:
            instructor_username = input("Enter instructor username: ")
            entered(types='-', count=10, final='no')

            # check if instructor username exists in the instructors csv
            instructors = read_csv("instructors.csv")
            instructor_exists = False
            for instructor in instructors:
                if instructor['username'] == instructor_username:
                    instructor_exists = True
                    break

            if instructor_exists:
                break
            else:
                entered(types='~', count=15, suffix='>', message="The instructor username couldn't be found. Please check it and try again before adding the course.", final='yes')

        # creates the course object and save it
        course = Course(course_number, title, instructor_username)

        # writes the course data to the CSV file
        write_csv("courses.csv", course)

        entered(types='*', count=10, message="Course added successfully.", final='yes')
        time.sleep(1)
        clear_terminal()



        #to view all information of the instroctor
    def view_instructors(self):
        instructors = read_csv("instructors.csv")
        clear_terminal()
        if not instructors:
            print("No instructors found.")
            time.sleep(2)
            return

        entered(types='_', count=25,  message= 'All Instructor',final='yes')  # "entered" to display a visual border for the section
        view_all_instructor_info(instructors)



    #to view all information of the course
    def view_courses(self):
        courses = read_csv("courses.csv")
        if not courses:
            print("No courses found.")
            return
        entered(types='_', count=25,  message= 'All courses',final='yes')
        view_all_course_info(courses)



        #to view all information of the enrollments
    def view_enrollments(self):
        enrollments = read_csv("enrollments.csv")
        if not enrollments:
            print("No enrollments found.")
            return
        entered(types='_', count=25,  message= 'All enrollments',final='yes')  # "entered" to display a visual border for the section
        view_all_enrollment_info(enrollments)



#to check for unique course numbers
def check_unique_course_number(file_name, course_number):
    data = read_csv(file_name)  # Assuming this uses csv.DictReader internally
    for row in data:
        if row['course_number'] == course_number:  # compare course numbers using the header
            return False
    return True


# to view all information
def view_students():
        students = read_csv("students.csv")
        if not students:
            print("No students found.")
            return
        clear_terminal()
        entered(types='_', count=25,  message= 'All Students',final='yes')  # "entered" to display a visual border for the section
        view_all_student_info(students)



##############################################################################################################################################################
#################### functions belows are to view all information of a user in a table #########################



#function to add perieds if the name or password is too long
def dot_names_string(name, max_length):
    #Shorten the string if it's too long and add '...' at the end.
    if len(name) > max_length:
        return name[:max_length - 3] + "..."
    return name


def view_all_student_info(all_students):
    # Fixed widths for each column
    first_names_width = 20
    last_names_width = 20
    usernames_width = 20
    passwords_width = 20

    print("| # | First Name           | Last Name            | Username             | Password             |")
    entered("-", 24, suffix='|')

    # display each student's details
    i = 0
    while i < len(all_students):
        student = all_students[i]
        first_name = dot_names_string(student['first_name'], first_names_width)
        last_name = dot_names_string(student['last_name'], last_names_width)
        username = dot_names_string(student['username'], usernames_width)
        password = dot_names_string(student['password'], passwords_width)

        student_number = i + 1  # to stores the student number

        # prints the student's details
        print("|", student_number, "|", first_name + " " * (first_names_width - len(first_name)), "|",
              last_name + " " * (last_names_width - len(last_name)), "|",
              username + " " * (usernames_width - len(username)), "|",
              password + " " * (passwords_width - len(password)), "|")
        i += 1  # Increment the counter to move to the next student

    entered("_", 24, suffix='|')


    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            clear_terminal()
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')










def view_all_instructor_info(all_instructors):
    # Fixed widths for each column
    first_names_width = 20
    last_names_width = 20
    usernames_width = 20
    titles_width = 20

    print("| # | First Name           | Last Name            | Username             | Title                |")
    entered("-", 24, suffix='|')

    # display each instructor's details
    i = 0
    while i < len(all_instructors):
        instructor = all_instructors[i]
        first_name = dot_names_string(instructor['first_name'], first_names_width)
        last_name = dot_names_string(instructor['last_name'], last_names_width)
        username = dot_names_string(instructor['username'], usernames_width)
        title = dot_names_string(instructor['title'], titles_width)

        instructor_number = i + 1  # This stores the instructor number

        # Print the instructor's details
        print("|", instructor_number, "|", first_name + " " * (first_names_width - len(first_name)), "|",
              last_name + " " * (last_names_width - len(last_name)), "|",
              username + " " * (usernames_width - len(username)), "|",
              title + " " * (titles_width - len(title)), "|")
        i += 1  # Increment the counter to move to the next instructor

    entered("_", 24, suffix='|')



    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            clear_terminal()
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')


def view_all_course_info(all_courses):
    # Fixed widths for each column
    course_numbers_width =15
    titles_width = 20
    instructors_width = 20

    print("| # | Course Number    | Title                | Instructor          |")
    entered("-", 22, suffix='|')

    # Display each course's details
    i = 0
    while i < len(all_courses):
        course = all_courses[i]
        course_number = dot_names_string(course['course_number'], course_numbers_width)
        title = dot_names_string(course['title'], titles_width)
        instructor = dot_names_string(course['instructor_username'], instructors_width)

        course_number_display = i + 1

        # Print the course's details
        print("|", course_number_display, "|", course_number + " " * (course_numbers_width - len(course_number)), "|",
              title + " " * (titles_width - len(title)), "|",
              instructor + " " * (instructors_width - len(instructor)), "|")
        i += 1  # Increment the counter to move to the next course

    entered("_", 22, suffix='|')

    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            clear_terminal()
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')












def view_all_enrollment_info(all_enrollments):
    # Fixed widths for each column
    student_usernames_width = 20
    course_numbers_width = 15

    # Display all enrollments until the user chooses to exit
    print("| # | Student Username     | Course Number     |")
    entered("-", 12, suffix='|')

    # Display each enrollment's details
    i = 0
    while i < len(all_enrollments):
        enrollment = all_enrollments[i]
        student_username = dot_names_string(enrollment['student_username'], student_usernames_width)
        course_number = dot_names_string(enrollment['course_number'], course_numbers_width)

        enrollment_number = i + 1  # This stores the enrollment number

        # Print the enrollment's details
        print("|", enrollment_number, "|", student_username + " " * (student_usernames_width - len(student_username)), "|",
              course_number + " " * (course_numbers_width - len(course_number)), "|")
        i += 1  # Increment the counter to move to the next enrollment

    entered("_", 12, suffix='|')

    while True:
        selection = input('Enter "h" to go back to the main menu: ').strip().lower()

        if selection == 'h':
            clear_terminal()
            return  # Exit the function to go back to the main menu
        else:
            entered('~', 10, suffix='>', message='Please enter "h" to go back.', final='yes')

