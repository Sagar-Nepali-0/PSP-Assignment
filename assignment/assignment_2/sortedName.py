'''
This function sorts a list of names alphabetically.
'''

def sort_names(names):
    """
    Sorts a list of names in alphabetical order.
    
    Args:
        names (list): List of names to sort
        
    Returns:
        list: Sorted list of names
    """
    # Use built-in sorted function with case-insensitive comparison
    return sorted(names, key=lambda x: x.lower())

# Test case
names = ["Alice", "Cob", "Bharlie", "dave"]
print(sort_names(names))