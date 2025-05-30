'''
employee_analysis.py
Performs various operations on employee data using Pandas.
'''

import pandas as pd
import numpy as np
from datetime import datetime

# Create DataFrame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John Smith', 'Alice Brown', 'Bob White', 'Emma Green', 'Charlie Red'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Age': [30, 28, 35, 40, 25],
    'Salary': [70000, 60000, 80000, 90000, 55000],
    'JoinDate': ['2018-07-15', '2020-03-10', '2016-11-01', '2012-05-25', '2021-06-01'],
    'ExperienceYears': [5, 3, 7, 11, 2]
}
df = pd.DataFrame(data)
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

# 9a: Select Name and Salary
print("Name and Salary:\n", df[['Name', 'Salary']])

# 9b: Filter IT Department
print("\nIT Department:\n", df[df['Department'] == 'IT'])

# 9c: Employees >30 and avg salary by dept
print("\nEmployees >30:\n", df[df['Age'] > 30])
print("\nAverage salary by department:\n", df.groupby('Department')['Salary'].mean())

# 9d: Count by department
print("\nEmployee count by department:\n", df['Department'].value_counts())

# 9e: Add Bonus column
df['Bonus'] = df['Salary'] * 0.1
print("\nWith Bonus column:\n", df)

# 9f: Replace HR with Human Resources
df['Department'] = df['Department'].replace('HR', 'Human Resources')
print("\nDepartment names updated:\n", df)

# 9g: Longest tenure
print("\nLongest tenure:\n", df[df['JoinDate'] == df['JoinDate'].min()])

# 9h: Salary categories
df['SalaryCategory'] = np.where(df['Salary'] > 75000, 'High', 'Low')
print("\nSalary categories:\n", df)

# 9i: Check duplicates
print("\nDuplicate EmployeeIDs:", df.duplicated('EmployeeID').any())
df.drop_duplicates('EmployeeID', inplace=True)

# 9j: Median age
print("\nMedian age:", df['Age'].median())