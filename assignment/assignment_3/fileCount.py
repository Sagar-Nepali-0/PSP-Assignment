"""
fileCount.py
------------
This program counts the number of words, lines, and characters in a file ('data.txt').
It handles file not found and other exceptions gracefully.
"""

filename = 'data.txt'

try:
    # Count words
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        print(f"Word count: {len(words)}")

    # Count lines
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Line count: {len(lines)}")

    # Count characters
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Character count: {len(content)}")
except FileNotFoundError:
    print(f"File '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
