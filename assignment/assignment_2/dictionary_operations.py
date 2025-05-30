'''
Various operations on dictionaries.
'''

def perform_dict_operations():
    """
    Demonstrates various dictionary operations.
    """
    # Initial dictionaries
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    
    # (a) Concatenate dictionaries
    nums = {**dic1, **dic2, **dic3}
    print("Concatenated:", nums)
    
    # (b) Add new key-value pair
    nums[7] = 70
    print("After adding (7,70):", nums)
    
    # (c) Update value for key 3
    nums[3] = 80
    print("After updating key 3:", nums)
    
    # (d) Remove third item (Python 3.7+ preserves insertion order)
    keys = list(nums.keys())
    if len(keys) >= 3:
        del nums[keys[2]]
    print("After removing third item:", nums)
    
    # (e) Sum all items
    sum_values = sum(nums.values())
    print("Sum of values:", sum_values)
    
    # (f) Multiply all items
    product = 1
    for value in nums.values():
        product *= value
    print("Product of values:", product)
    
    # (g) Max and min values
    print(f"Max: {max(nums.values())}, Min: {min(nums.values())}")

perform_dict_operations()