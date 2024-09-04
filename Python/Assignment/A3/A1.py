class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Availability status of the book

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Status: {status}"

class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []  # List to keep track of borrowed books

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} has not borrowed any books.")

class Library:
    def __init__(self):
        self.books = []  # Collection of books in the library
        self.members = []  # List of library members

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"{member.name} has been registered as a member of the library.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available in the library.")

    def list_borrowed_books(self):
        borrowed_books = [book for book in self.books if not book.available]
        if borrowed_books:
            print("Borrowed books in the library:")
            for book in borrowed_books:
                print(f"- {book}")
        else:
            print("No books are currently borrowed.")

# Example usage:
# Create a library instance
library = Library()

# Create some books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567891")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567892")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register a new member
member1 = Member("Alice", "M001")
library.register_member(member1)

# Member borrows a book
member1.borrow_book(book1)

# List all available books
library.list_available_books()

# List all borrowed books by a member
member1.list_borrowed_books()

# Member returns a book
member1.return_book(book1)

# List all available books after return
library.list_available_books()

# List all borrowed books in the library
library.list_borrowed_books()
