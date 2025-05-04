"""
file name: utilities.py


Problem Description:

Mini Registrar System
A simple system with Admin, Student, and Instructor modules.
Admin can add students, instructors, and courses, and view data.
Students can enroll in courses and view their enrollments.
Instructors can see the courses they teach. Data is stored in CSV files.

variable name:
"file_name"            wich file file to open or save to
"data"                 To store the rows read from the file
"file"                 To open the file for reading or writing
"reader"               To read through file
"row"                  each row of data from the file
"headers"              To list the column names for the data
"obj"                  To represent the object that are being saved to the fil like Student, Instructor, etc.
"Student"              the student object type
"Instructor"           the instructor object type
"Course"               the enrollment object type
"Enrollment"           the enrollment object type
"password"             To store a user's password
"username"             To store a user's username
"user"                 To represent a user like Student or Instructor
"types"                to display which symbol
"count"                To set how many times the symbol repeats when printing
"suffix"               To add a text in the middle of the printed symbols
"message"              To display a message inside the the printed symbols
"final"                To decide whether to print the symbols again
"attempts"             To count the login attempts
"users"                To store the list of users from the file


First Create Date: Nov21, 2024
Last Update Date: dec 10, 2024
Author: aksblue
Version: 1.0
"""


import csv
import os
from classes import Student, Instructor, Course, Enrollment



# Function to read data from a CSV file
def read_csv(file_name):
    data = []
    try:
        with open(file_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)  # Append each row as a dictionary to the list
    except:
        return []  # If the file doesn't exist, return an empty list
    return data


######################################
#function to write to a file

def write_csv(file_name, obj):
    headers = {
        Student: ['first_name', 'last_name', 'username', 'password'],
        Instructor: ['first_name', 'last_name', 'username', 'password', 'title'],
        Course: ['course_number', 'title', 'instructor_username'],
        Enrollment: ['student_username', 'course_number']
    }

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        # Add headers if the file is empty
        if os.stat(file_name).st_size == 0:
            writer.writerow(headers[type(obj)])

        # Write object data to the file
        if isinstance(obj, Student):
            writer.writerow([obj.first_name, obj.last_name, obj.username, obj.password])
        elif isinstance(obj, Instructor):
            writer.writerow([obj.first_name, obj.last_name, obj.username, obj.password, obj.title])
        elif isinstance(obj, Course):
            writer.writerow([obj.course_number, obj.title, obj.instructor])
        elif isinstance(obj, Enrollment):
            writer.writerow([obj.student_username, obj.course_number])


######################################################################################################################
# Function to check if a username or password is unique in a CSV file


def is_unique_password(file_name, password):
    rows = read_csv(file_name)
    for row in rows:
        if row['password'] == password:
            return False # If username already exists, return False
    return True  # Return True if password is unique


def is_unique_username(file_name, username):

    rows = read_csv(file_name)
    for row in rows:
        if row['username'] == username:
            return False # If username already exists, return False
    return True  # Return True if username is unique


##################################################################################################

# Function to verify if the user's username and password match
def verify_user(user, username, password):
    return user.username == username and user.password == password

######################################################################



#function to design
def entered(types='*', count=5, suffix=' ', message='', final = 'no'):
    # Multiply the symbol by 4 * count for the length of the border
    stars = types * 4 * count
    print(stars + suffix)  # Print the pattern with the suffix

    if message:  # If a message is provided
        # put the message in the center
        message_line = message.center(4 * count)
        print(message_line)
    if final=='yes':
        print(stars + suffix)  # Optional to print the pattern again to close it off

###################################################################################################



# Function to handle login attempts for a user limits to 5 attempts
def login_attempts(user_class, file_name):
    attempts = 0  # Set limit for attempts
    while attempts < 5: #stops once attemtpts is 4
        if attempts == 0:
            entered(types='=', count=15, suffix='+', message='====== type "exit" to quit ======', final='yes') #designs to tell them how to exit

        username = input("\nEnter username: ")
        entered()
        if username.lower() == 'exit':
            print("See you next time!")
            return None
        password = input("Enter password: ")  # inpu password correctly
        if password.lower() == 'exit':
            return None
        users = read_csv(file_name)  # Get the list of users from the file
        for row in users:
            if user_class == Instructor:
                # For Instructor pass title as well
                user = user_class(row['first_name'], row['last_name'], row['username'], row['password'], row['title'])
            else:
                user = user_class(row['first_name'], row['last_name'], row['username'], row['password'])  # For other user classes

            if verify_user(user, username, password):  # check if username and password match
                return user  # Return the user object if the login was successful

        attempts += 1 # Increase attempts after each failed login

        if attempts < 5:
            entered(types='~', count=15, suffix='>', message='Incorrect username or password. Please try again.', final='yes')# error message for incorrect password or username

    entered(types='=', count=30, suffix='+', message='Too many failed attempts. Please try again later!', final='yes')# error message for to mamy attempts

    return None  # Return None if login fails after 5 attempts


#################################################################################################################################
#functions to clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



