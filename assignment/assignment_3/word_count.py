"""
word_count.py
-------------
This program reads a text file ('data.txt'), removes punctuation, and counts the frequency of each word.
It prints the word frequencies in a readable tabular format. Handles file not found and other exceptions gracefully.
"""

import string
from collections import Counter

try:
    with open('data.txt', 'r') as file:
        # Read the file content and convert to lowercase
        line = file.read().lower()
        # Remove punctuation
        clean_line = line.translate(str.maketrans('', '', string.punctuation))
        # Split into words
        words = clean_line.split()
        # Count word frequencies
        word_counts = Counter(words)
        # Print the word counts in tabular format
        print("Word\t\tCount")
        print("-" * 24)
        for word, count in word_counts.items():
            print(f"{word:<15}{count}")
except FileNotFoundError:
    print("File 'data.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")