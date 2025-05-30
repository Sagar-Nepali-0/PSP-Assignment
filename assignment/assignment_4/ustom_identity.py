'''
custom_identity.py
Attempts to create a 3x4 identity matrix (rectangular diagonal matrix).
'''

import numpy as np

def custom_identity_matrix():
    """
    Creates a 3x4 matrix with ones on the main diagonal.
    
    Returns:
        numpy.ndarray: 3x4 diagonal matrix
    """
    return np.eye(3, 4)

print("3x4 Diagonal Matrix:\n", custom_identity_matrix())