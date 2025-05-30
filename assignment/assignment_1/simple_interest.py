'''
simple_interest.py  
Calculates simple interest given principal, rate, and time.  

Input:  
- Principal amount (float)  
- Rate of interest (float)  
- Time period (float)  

Output:  
- Simple interest  

Formula:  
SI = (P * R * T) / 100  

Example:  
Input: 1000, 5, 2  
Output: "100.0"  
'''

# Take input for principal, rate, and time from the user
principle = int(input("Enter principle value: "))
rate = int(input("Enter rate value(%): "))
time = int(input("Enter duration of time(month): "))

# Calculate simple interest using the formula
SI = (principle * rate * time) / 100

# Print the calculated simple interest
print(f'Simple Interest (SI): {SI}')