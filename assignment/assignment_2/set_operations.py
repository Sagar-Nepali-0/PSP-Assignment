'''
Demonstrates various set operations.
'''

def perform_set_operations():
    """
    Demonstrates set operations including union, intersection, etc.
    """
    set1 = {20, 40, 60}
    set2 = {10, 20, 30, 40, 50, 60}
    
    # (a) Union and length
    union_set = set1.union(set2)
    print(f"Union: {union_set}, Length: {len(union_set)}")
    
    # (b) Intersection
    print("Intersection:", set1.intersection(set2))
    
    # (c) Symmetric difference
    print("Symmetric difference:", set1.symmetric_difference(set2))
    
    # (d) Add 40 to set1
    set1.add(40)  # Already exists, no change
    print("After adding 40:", set1)
    
    # (e) Remove 20 from set2
    set2.remove(20)
    print("After removing 20 from set2:", set2)

perform_set_operations()