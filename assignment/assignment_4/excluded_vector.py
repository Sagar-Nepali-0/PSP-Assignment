'''
excluded_vector.py
Creates a vector of size 10 with values between 0 and 1 (both excluded).
'''

import numpy as np

def create_excluded_vector():
    """
    Creates a 10-element vector with values in (0,1).
    
    Returns:
        numpy.ndarray: Resulting vector
    """
    return np.linspace(0, 1, num=11, endpoint=False)[1:11]

print("Vector (0,1):\n", create_excluded_vector())