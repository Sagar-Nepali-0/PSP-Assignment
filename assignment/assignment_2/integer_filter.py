'''
This program filters integers between 1-100 from user input.
'''

def get_valid_integers():
    """
    Gets integers from user and returns only those between 1-100.
    
    Returns:
        list: Valid integers entered by user
    """
    numbers = []
    print("Enter integers (type 'done' to finish):")
    
    while True:
        user_input = input()
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            if 1 <= num <= 100:
                numbers.append(num)
        except ValueError:
            print("Please enter a valid integer")
            
    return numbers

# Test case
valid_numbers = get_valid_integers()
print("Valid numbers:", valid_numbers)