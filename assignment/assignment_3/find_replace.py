"""
find_replace.py
---------------
This program finds and replaces a specific word in a file ('data.txt') with another word entered by the user.
It reads the file, performs the replacement, writes the updated content back, and handles file-related exceptions.
"""

filename = 'data.txt'

try:
    # Read the file content
    with open(filename, 'r') as file:
        content = file.read()

    # Ask user for the word to find and the replacement
    select_word = input("Select word to replace: ")
    if select_word in content:
        replace_word = input("Replace with: ")
        # Replace all occurrences
        new_content = content.replace(select_word, replace_word)
        # Write the new content back to the file
        with open(filename, 'w') as file:
            file.write(new_content)
        print("Replacement done.\n")
        print(new_content)
    else:
        print("Word not found in file.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")