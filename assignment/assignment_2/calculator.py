'''
This module provides basic arithmetic operations.
'''

def add(a, b):
    """Returns sum of two numbers"""
    return a + b

def subtract(a, b):
    """Returns difference between two numbers"""
    return a - b

def multiply(a, b):
    """Returns product of two numbers"""
    return a * b

def divide(a, b):
    """Returns division result, handles division by zero"""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def floor_divide(a, b):
    """Returns floor division result"""
    return a // b

def modulus(a, b):
    """Returns remainder of division"""
    return a % b

def power(a, b):
    """Returns a raised to power of b"""
    return a ** b

# Test cases
print(f"Add: {add(5, 3)}")          # 8
print(f"Subtract: {subtract(5, 3)}")     # 2
print(f"Multiply: {multiply(5, 3)}")     # 15
print(f"Divide: {divide(5, 0)}")       # Error message
print(f"Floor Divide: {floor_divide(5, 3)}") # 1
print(f"Modulus: {modulus(5, 3)}")      # 2
print(f"Power: {power(5, 3)}")        # 125