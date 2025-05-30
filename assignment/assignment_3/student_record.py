"""
student_record.py
-----------------
This program defines a Student class with attributes such as id, name, address, admission year, level, and section.
It takes input for all attributes from the user, creates a Student object, and displays the student's details.
"""

class Student:
    def __init__(self):
        # Input validation for id
        while True:
            try:
                self.id = int(input("Enter id: "))
                break
            except ValueError:
                print("Please enter a valid integer for id.")
        self.name = input('Enter name: ')
        self.address = input("Enter address: ")
        # Input validation for admission year
        while True:
            try:
                self.admission_year = int(input("Enter admission year: "))
                break
            except ValueError:
                print("Please enter a valid year.")
        self.level = input("Enter level: ")
        self.section = input("Enter section: ")
    
    def display_student(self):
        # Display student details in a formatted way
        print("\nStudent Details:")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Create and display a student
student1 = Student()
student1.display_student()