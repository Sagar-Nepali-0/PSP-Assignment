'''
This function checks if a number is prime.
'''

def is_prime(number):
    """
    Determines if a number is prime.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if number <= 1:
        return False
    # Check for factors from 2 to square root of number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Test case
print(is_prime(17))  # Should return True
print(is_prime(15))  # Should return False