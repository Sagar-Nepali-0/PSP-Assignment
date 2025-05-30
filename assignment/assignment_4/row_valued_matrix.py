'''
row_valued_matrix.py
Creates a 5x5 matrix with row values ranging from 0 to 4.
'''

import numpy as np

def create_row_matrix():
    """
    Creates matrix where each row contains values 0-4.
    
    Returns:
        numpy.ndarray: 5x5 matrix
    """
    return np.tile(np.arange(5), (5, 1))

print("Row-valued matrix:\n", create_row_matrix())