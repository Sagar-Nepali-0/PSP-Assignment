'''
divisible_7_multiple_5.py  
Finds numbers between 1500 and 2000 divisible by 7 and multiples of 5.  

Input:  
- None (range is fixed: 1500-2000)  

Output:  
- Prints all matching numbers  

Example Output:  
1505, 1540, 1575, ..., 1995  
'''

# Loop through numbers from 1500 to 2000 (inclusive)
for i in range(1500, 2000 + 1):
    # Check if the number is divisible by both 7 and 5
    if (i % 7 == 0 and i % 5 == 0):
        print(i)