class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("-" * 20)

    def update_author(self, new_author):
        self.author = new_author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                # Simulate lending by reducing copies (assuming copies attribute)
                # book.copies -= 1 
                print(f"{book_title} has been lent.")
                return
        print(f"{book_title} is not available in the library.")

    def display_available_books(self):
        print("Available Books:")
        for book in self.books:
            book.display_info()

if __name__ == "__main__":
    
    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780261102354")
    book2 = Book("1984", "George Orwell", "9780452003424")

    # Create a library
    library = Library()

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)

    # Display available books
    library.display_available_books()

    # Lend a book
    library.lend_book("The Lord of the Rings") 

    # Display available books after lending
    library.display_available_books()

    # Update book author
    book1.update_author("J.R.R. Tolkien (edited)")
    book1.display_info()
