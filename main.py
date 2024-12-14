class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Pages: {self.pages}"


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

    def menu(self):
        while True:
            print("\nLibrary Menu:")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Search Book by Title")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = int(input("Enter year of publication: "))
                isbn = input("Enter book ISBN: ")
                pages = int(input("Enter number of pages: "))
                book = Book(title, author, year, isbn, pages)
                self.add_book(book)
            elif choice == '2':
                self.display_books()
            elif choice == '3':
                title = input("Enter title to search: ")
                self.search_by_title(title)
            elif choice == '4':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Main Program
if __name__ == "__main__":
    library = Library()
    library.menu()
