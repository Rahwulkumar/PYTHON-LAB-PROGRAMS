# main_LibraryManager.py

from LibraryManager import LibraryManager

# Initialize LibraryManager
library = LibraryManager()

# Sample books data (ISBN: Book details)
books_data = {
    "978-3-16-148410-0": {
        "title": "Operating Systems Concepts",
        "author": "Abraham Silberschatz",
        "publisher": "Wiley",
        "volume": 10,
        "year_of_publication": 2020
    },
    "978-0-13-467095-9": {
        "title": "Data Structures and Algorithm Analysis",
        "author": "Mark Allen Weiss",
        "publisher": "Pearson",
        "volume": 4,
        "year_of_publication": 2022
    },
    "978-1-59327-856-2": {
        "title": "Machine Learning with Python",
        "author": "Andreas C. Müller",
        "publisher": "O'Reilly Media",
        "volume": 2,
        "year_of_publication": 2023
    },
    # Add more books here
}

# Adding books to the library
for isbn, details in books_data.items():
    library.add_book(isbn, details["title"], details["author"], details["publisher"], details["volume"], details["year_of_publication"])

# List all books
print("All Books:")
for book in library.list_books():
    print(book)
print()

# Retrieve and display details of a book by ISBN
print("Details of a Book (ISBN 978-3-16-148410-0):")
print(library.get_book_details("978-3-16-148410-0"))
print()

# Search for books by title
print("Search Books by Title ('Operating'):")
for book in library.search_books("Operating"):
    print(book)
print()

# Search for books by author
print("Search Books by Author ('Mark Allen Weiss'):")
for book in library.search_books("Mark Allen Weiss", search_by='author'):
    print(book)
print()

# Update a book's details
print("Update Book (ISBN 978-3-16-148410-0):")
library.update_book("978-3-16-148410-0", volume=11, year_of_publication=2021)
print(library.get_book_details("978-3-16-148410-0"))
print()

# Check if a book is available in the library by ISBN
print("Check if Book (ISBN 978-3-16-148410-0) is Available:")
print(library.is_book_available("978-3-16-148410-0"))
print()

# Remove a book from the library by ISBN
print("Remove Book (ISBN 978-3-16-148410-0):")
library.remove_book("978-3-16-148410-0")
print(library.get_book_details("978-3-16-148410-0"))
print()

# List all books after removal
print("All Books After Removal:")
for book in library.list_books():
    print(book)
print()
