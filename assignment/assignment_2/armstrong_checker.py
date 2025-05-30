'''
This function checks if a number is an Armstrong number.
'''

def is_armstrong(number):
    """
    Checks if a number is Armstrong number.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if Armstrong, False otherwise
    """
    num_str = str(number)
    length = len(num_str)
    total = 0
    
    # Calculate sum of digits raised to power of number length
    for digit in num_str:
        total += int(digit)**length
        
    return total == number

# Test case
print(is_armstrong(153))  # True (1³ + 5³ + 3³ = 153)
print(is_armstrong(123))  # False