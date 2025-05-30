'''
euclidean_distance.py  
Calculates the Euclidean distance between two 2D points.  

Input:  
- Coordinates (x1, y1) and (x2, y2)  

Output:  
- Distance between the two points  

Formula:  
distance = √((x2 - x1)² + (y2 - y1)²)  

Example:  
Input: (3, 4), (7, 1)  
Output: "5.0"  
'''
from math import sqrt

# Take input for the first point and split into x and y coordinates
first_coordinates_x, first_coordinates_y = input("x1, y1: ").split()
# Take input for the second point and split into x and y coordinates
second_coordinates_x, second_coordinates_y = input("x2, y2: ").split()

# Convert input strings to integers for calculation
first_coordinates_x = int(first_coordinates_x)
first_coordinates_y = int(first_coordinates_y)
second_coordinates_x = int(second_coordinates_x)
second_coordinates_y = int(second_coordinates_y)

# Calculate Euclidean distance using the formula
distance = sqrt((second_coordinates_x - first_coordinates_x)**2 + (second_coordinates_y - first_coordinates_y)**2)
# Print the calculated distance
print(f"The distance beteen two are is: {distance}")