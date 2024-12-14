from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("\nBook added successfully!")

    def display_books(self):
        if not self.books:
            print("\nNo books in the library.")
        else:
            print("\nBooks in the library:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def search_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                print(book)
        else:
            print("\nNo books found with that title.")
