'''
This function counts the number of uppercase and lowercase letters in a given string.
'''

def count_case_letters(input_string):
    """
    Counts uppercase and lowercase letters in a string.
    
    Args:
        input_string (str): The string to analyze
        
    Returns:
        tuple: (uppercase_count, lowercase_count)
    """
    upper = 0
    lower = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
            
    return upper, lower

# Test case
test_str = "Hello World"
upper, lower = count_case_letters(test_str)
print(test_str)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")