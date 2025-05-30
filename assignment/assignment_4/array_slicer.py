'''
array_slicer.py
Sorts user-input array and performs slicing operations.
'''

import numpy as np

def array_operations():
    """
    Takes user input, sorts array, and performs slicing.
    """
    elements = input("Enter numbers separated by spaces: ")
    arr = np.array([float(x) for x in elements.split()])
    arr.sort()
    
    print("\nSorted array:", arr)
    print("Slice 2-5:", arr[2:5])
    print("Slice 5-8:", arr[5:8])
    print("Slice 2-9:", arr[2:9])

array_operations()