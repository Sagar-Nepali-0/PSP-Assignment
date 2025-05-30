'''
count_letters_digits.py  
Counts the number of letters and digits in a given string.  

Input:  
- A string (e.g., "Hello123")  

Output:  
- Number of letters  
- Number of digits  

Example:  
Input: "Hello123"  
Output: "Letters: 5, Digits: 3"  
'''

# Initialize counters for digits and letters
digit = 0
letter = 0

# Take input string from user
string_input = input("Enter a string: ")
# Iterate through each character in the input string
for string in string_input:
    # Check if the character is a digit
    if string.isdigit():
        digit += 1
    # Check if the character is a letter
    elif string.isalpha():
        letter += 1
# Print the counts of digits and letters
print(f"Word: {string_input}")
print(f"Letter: {letter}, Digit: {digit}")
