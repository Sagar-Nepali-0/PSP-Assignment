'''
This program counts occurrences of letter 'a' in a list of names.
'''

def count_a_in_names():
    """
    Gets names from user and counts occurrences of letter 'a'.
    
    Returns:
        int: Count of 'a' letters in all names
    """
    names = []
    print("Enter names (type 'done' to finish):")
    
    while True:
        name = input()
        if name.lower() == 'done':
            break
        names.append(name.lower())  # Convert to lowercase for case-insensitive count
    
    a_count = sum(name.count('a') for name in names)
    return a_count

# Test case
print("Total 'a's:", count_a_in_names())