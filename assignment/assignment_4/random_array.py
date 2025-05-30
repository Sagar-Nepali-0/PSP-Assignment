'''
random_array.py
Generates a random array of user-specified shape and computes its average.
'''

import numpy as np

def generate_random_array():
    """
    Takes user input for array dimensions, generates random array, and computes average.
    """
    a = int(input("Enter first dimension (a): "))
    b = int(input("Enter second dimension (b): "))
    
    # Generate random array with values between 0 and 1
    random_array = np.random.rand(a, b)
    average = np.mean(random_array)
    
    print("\nGenerated array:\n", random_array)
    print("\nAverage of array:", round(average, 2))

generate_random_array()