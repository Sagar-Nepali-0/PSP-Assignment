'''
This program compares two lists of integers.
'''

def compare_lists(list1, list2):
    """
    Compares two lists and prints comparison results.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    """
    # Length comparison
    print(f"Same length: {len(list1) == len(list2)}")
    
    # Sum comparison
    print(f"Same sum: {sum(list1) == sum(list2)}")
    
    # Common elements
    common = set(list1) & set(list2)
    print(f"Common elements: {common if common else 'None'}")

# Test case
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]
compare_lists(list1, list2)