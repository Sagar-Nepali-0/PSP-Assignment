'''
series_operations.py
Performs arithmetic operations on two Pandas Series.
'''

import pandas as pd

def series_math():
    """
    Creates two Series and demonstrates arithmetic operations.
    """
    series1 = pd.Series([2, 4, 6, 8])
    series2 = pd.Series([1, 3, 5, 7])
    
    print("Addition:\n", series1 + series2)
    print("\nSubtraction:\n", series1 - series2)
    print("\nMultiplication:\n", series1 * series2)
    print("\nDivision:\n", series1 / series2)

series_math()