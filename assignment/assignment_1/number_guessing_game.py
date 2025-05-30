'''
number_guessing_game.py  
A game where the user guesses a random number (1-100) within 5 attempts.  

Features:  
- Generates a random number  
- Gives hints ("Too high", "Too low")  
- Ends after 5 wrong guesses  

Example:  
Input: 50 (Too low)  
Input: 75 (Too high)  
...  
Output: "Correct! You won!" or "Game Over! The number was X."  
'''

from random import randrange

MAX = 100
MIN = 1
MAX_ATTEMPTS = 5  # Maximum allowed attempts

# Generate a random number between MIN and MAX (inclusive)
generate_randomNumber = randrange(MIN, MAX + 1)

# Initialize attempt counter
count = 0

# Loop for a maximum of MAX_ATTEMPTS
while count < MAX_ATTEMPTS:
    # Take guess from the user
    if count == 0:
        user_guess = int(input(f"Guess number between {MIN}-{MAX}: "))
    else:
        user_guess = int(input("Try again: "))

    count += 1

    # Check if the guess is correct
    if user_guess == generate_randomNumber:
        print(f"You win in {count} attempt(s).")
        break
    elif user_guess > generate_randomNumber:
        print("Too high.")
    else:
        print("Too low")

# If user didn't guess correctly in allowed attempts
if user_guess != generate_randomNumber:
    print(f"Game Over! The number was {generate_randomNumber}.")



