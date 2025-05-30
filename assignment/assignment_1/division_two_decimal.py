'''
division_two_decimals.py  
Divides two numbers and displays the result rounded to 2 decimal places.  

Input:  
- Two integers (dividend and divisor)  

Output:  
- Division result formatted to 2 decimal places  

Example:  
Input: 10, 3  
Output: "3.33"  
'''

dividend = int(input("Enter Dividend value: ")) # dividend value
divisor = int(input("Enter Divisor value: ")) # divisor value

result = float(dividend/divisor) # convert value to float
print(f"{dividend} ÷ {divisor} = {result:.2f}") # :.2f, display 2 decimal value eg: 3.42, 5.00 etc.