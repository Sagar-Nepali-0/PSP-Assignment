"""
copy_content.py
---------------
This program copies the contents of one file ('data.txt') to another file ('duplicate.txt').
It uses the shutil module for file operations and handles common file-related exceptions.
"""

import shutil

original_file = 'data.txt'
copy_file = 'duplicate.txt'

try:
    # Copy the contents of original_file to copy_file
    shutil.copyfile(original_file, copy_file)
    print(f"Contents copied from '{original_file}' to '{copy_file}'.")
except FileNotFoundError:
    print(f"Source file '{original_file}' not found.")
except PermissionError:
    print("Permission denied while accessing the files.")
except Exception as e:
    print(f"An error occurred: {e}")

