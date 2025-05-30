''' 
Determines if a given number is odd or even.  

Input:  
- An integer number from the user  

Output:  
- Prints whether the number is odd or even  

Example:  
Input: 7  
Output: "7 is odd"  
'''

user_input = int(input("Enter a number: ")) # user enter the number
print(f"{user_input} is even") if user_input % 2 == 0 else print(f"{user_input} is odd") # display result as condition