"""
library_manage.py
-----------------
A simple library management system using OOP and file handling.

Features:
- Display all books
- Search for a book by title
- Issue a book (mark as issued)
- Return a book (mark as available)
- Persistent storage using CSV file
"""

import csv

class Library:
    """
    Library class to manage book records.
    """
    def __init__(self, filename):
        """
        Initialize the Library with a filename for storage.
        Loads books from the CSV file.
        """
        self.filename = "book.csv"  # Always use 'book.csv' for storage
        self.books = self.load_books()

    def load_books(self):
        """
        Load books from the CSV file.
        Returns a list of book dictionaries.
        """
        books = []
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    books.append(row)
        except FileNotFoundError:
            print(f"{self.filename} is not found. Starting with an empty library.")
        return books

    def save_books(self):
        """
        Save the current list of books to the CSV file.
        """
        if not self.books:
            return
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['Title', 'Author', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow(book)

    def display_books(self):
        """
        Display all books in the library.
        """
        if not self.books:
            print("No books in the library.")
            return
        print("\nAll Books:")
        for book in self.books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Status: {book['Status']}")

    def search_book(self, title):
        """
        Search for a book by title (case-insensitive, partial match).
        Prints details if found.
        """
        found = False
        for book in self.books:
            if title.lower() in book['Title'].lower():
                print(f"\nTitle : {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Status: {book['Status']}")
                found = True
        if not found:
            print("Book not found.")

    def issue_book(self, title):
        """
        Issue a book if available. Changes status to 'issued'.
        """
        for book in self.books:
            if title.lower() == book['Title'].lower():
                if book['Status'].lower() == 'available':
                    book['Status'] = 'issued'
                    self.save_books()
                    print(f"Book '{book['Title']}' issued successfully.")
                    return
                else:
                    print(f"Book '{book['Title']}' is already issued.")
                    return
        print("Book not found.")

    def return_book(self, title):
        """
        Return a book if it was issued. Changes status to 'available'.
        """
        for book in self.books:
            if title.lower() == book['Title'].lower():
                if book['Status'].lower() == 'issued':
                    book['Status'] = 'available'
                    self.save_books()
                    print(f"Book '{book['Title']}' returned successfully.")
                    return
                else:
                    print(f"Book '{book['Title']}' was not issued.")
                    return
        print("Book not found.")

# Create Library instance with 'books.csv' as storage
lib = Library("books.csv")

# Main menu loop
while True:
    print("\n1. Display All Books\n2. Search\n3. Issue\n4. Return\n5. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        lib.display_books()
    elif choice == "2":
        title = input("Enter title to search: ").strip()
        lib.search_book(title)
    elif choice == "3":
        title = input("Enter title to issue: ").strip()
        lib.issue_book(title)
    elif choice == "4":
        title = input("Enter title to return: ").strip()
        lib.return_book(title)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
