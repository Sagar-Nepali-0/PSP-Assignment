'''
celsius_to_fahrenheit.py  
Converts a temperature in Celsius to Fahrenheit.  

Input:  
- A float number (temperature in Celsius)  

Output:  
- Converted temperature in Fahrenheit  

Formula:  
F = (C * 9/5) + 32  

Example:  
Input: 25  
Output: "77.0°F"  
'''

# Take input from user for temperature in Celsius
celsius = int(input("Enter temperature in Celsius(°C): "))

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (9/5 * celsius) + 32

# Print the result in Fahrenheit
print(f"Temperature: {fahrenheit}°F")