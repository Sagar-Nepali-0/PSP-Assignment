'''
null_vector.py
Creates a null vector of size 10 with the fifth value as 1.
'''

import numpy as np

def create_null_vector():
    """
    Creates a null vector of size 10 with fifth element as 1.
    
    Returns:
        numpy.ndarray: Resulting vector
    """
    vector = np.zeros(10)  # Create vector of zeros
    vector[4] = 1  # Set fifth element (index 4) to 1
    return vector

# Execute and print
result = create_null_vector()
print("Null vector with fifth value as 1:\n", result)