"""
employes.py
-----------
A program to manage employee records: add new employees and view all employees.
Stores data in 'employees.csv' using CSV format and handles file errors.
"""

import csv

class Employee:
    """
    Employee class to store employee details.
    """
    def __init__(self):
        # Collect employee details from user with input validation
        self.empid = input("Enter Empid: ")
        self.name = input("Enter name: ")
        self.address = input("Enter address: ")
        self.contact_number = input("Enter contact number: ")
        self.spouse_name = input("Enter spouse name: ")
        # Validate number_of_children as integer
        while True:
            try:
                self.number_of_children = int(input("Enter number of children: "))
                break
            except ValueError:
                print("Please enter a valid integer for number of children.")
        # Validate salary as float
        while True:
            try:
                self.salary = float(input("Enter salary: "))
                break
            except ValueError:
                print("Please enter a valid number for salary.")

    def as_dict(self):
        # Return employee details as a dictionary
        return {
            "EmpID": self.empid,
            "Name": self.name,
            "Address": self.address,
            "Contact Number": self.contact_number,
            "Spouse Name": self.spouse_name,
            "Number of Children": self.number_of_children,
            "Salary": self.salary
        }

def add_employee():
    """
    Add a new employee and write to CSV file.
    """
    emp = Employee()
    try:
        with open('employees.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=emp.as_dict().keys())
            # Write header only if file is empty
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(emp.as_dict())
        print("Employee added successfully!")
    except Exception as e:
        print("Error writing to file:", e)

def view_employees():
    """
    Display all employees from the CSV file in a tabular format.
    """
    try:
        with open('employees.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows:
                print("No employee records found.")
                return
            # Print header
            headers = reader.fieldnames
            col_widths = [max(len(str(row[h])) for row in rows + [dict(zip(headers, headers))]) for h in headers]
            header_row = " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
            print(header_row)
            print("-+-".join('-' * w for w in col_widths))
            # Print each employee row
            for row in rows:
                print(" | ".join(str(row[h]).ljust(col_widths[i]) for i, h in enumerate(headers)))
    except FileNotFoundError:
        print("No employee records found.")

# Main menu loop
while True:
    print("\n1. Add Employee\n2. View Employees\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
