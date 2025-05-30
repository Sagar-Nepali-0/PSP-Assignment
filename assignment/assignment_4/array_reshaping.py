'''
array_reshaping.py
Creates, sorts, and reshapes a random integer array.
'''

import numpy as np

def reshape_array():
    """
    Generates random array, sorts it, and reshapes it.
    """
    size = int(input("Enter array size (>=10): "))
    arr = np.random.randint(1, 100, size)
    arr.sort()
    
    print("\nOriginal array:\n", arr)
    
    # Find possible shapes
    factors = [i for i in range(2, size) if size % i == 0]
    if factors:
        rows = factors[0]
        cols = size // rows
        reshaped = arr.reshape(rows, cols)
        print(f"\nReshaped to {rows}x{cols}:\n", reshaped)
    else:
        print("Cannot reshape - prime number of elements")

reshape_array()