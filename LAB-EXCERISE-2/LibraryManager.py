# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year_of_publication):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year_of_publication': year_of_publication
            }

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
        else:
            print(f"No book found with ISBN {isbn}.")

    def get_book_details(self, isbn):
        return self.books.get(isbn, f"No book found with ISBN {isbn}.")

    def search_books(self, keyword, search_by='title'):
        results = []
        for book in self.books.values():
            if keyword.lower() in book[search_by].lower():
                results.append(book)
        return results

    def list_books(self):
        return list(self.books.values())

    def update_book(self, isbn, **kwargs):
        if isbn in self.books:
            for key, value in kwargs.items():
                if key in self.books[isbn]:
                    self.books[isbn][key] = value
                else:
                    print(f"Invalid attribute: {key}")
        else:
            print(f"No book found with ISBN {isbn}.")

    def is_book_available(self, isbn):
        return isbn in self.books
