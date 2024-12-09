class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Status: {status}"


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        print(f"'{title}' has been added to the library.")

    def register_member(self, name, membership_id):
        self.members.append(Member(name, membership_id))
        print(f"{name} has been registered as a member.")

    def find_member(self, name):
        return next((m for m in self.members if m.name == name), None)

    def find_book(self, title):
        return next((b for b in self.books if b.title == title), None)

    def list_books(self, available=True):
        books = [book for book in self.books if book.available == available]
        if books:
            status = "Available" if available else "Borrowed"
            print(f"{status} books:")
            for book in books:
                print(f"- {book}")
        else:
            print(f"No {'available' if available else 'borrowed'} books.")


def menu():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Available Books")
        print("6. List Borrowed Books")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            library.add_book(title, author, isbn)

        elif choice == '2':
            name = input("Enter member name: ").strip()
            membership_id = input("Enter membership ID: ").strip()
            library.register_member(name, membership_id)

        elif choice == '3':
            name = input("Enter member name: ").strip()
            member = library.find_member(name)
            if member:
                title = input("Enter book title: ").strip()
                book = library.find_book(title)
                if book:
                    member.borrow_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == '4':
            name = input("Enter member name: ").strip()
            member = library.find_member(name)
            if member:
                title = input("Enter book title: ").strip()
                book = library.find_book(title)
                if book:
                    member.return_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == '5':
            library.list_books(available=True)

        elif choice == '6':
            library.list_books(available=False)

        elif choice == '7':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


menu()

""" class Book:
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

# Menu-driven program with inline validation
def menu():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Books")
        print("2. Register a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. List Available Books")
        print("6. List Borrowed Books")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Ask how many books the user wants to add
            while True:
                try:
                    num_books = int(input("How many books do you want to add? ").strip())
                    if num_books < 1:
                        print("Please enter a number greater than or equal to 1.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            
            for _ in range(num_books):
                while True:
                    title = input("Enter the book title: ").strip()
                    if title:
                        break
                    print("Book title cannot be empty.")
                while True:
                    author = input("Enter the author: ").strip()
                    if author:
                        break
                    print("Author cannot be empty.")
                while True:
                    isbn = input("Enter the ISBN: ").strip()
                    if isbn:
                        break
                    print("ISBN cannot be empty.")
                book = Book(title, author, isbn)
                library.add_book(book)

        elif choice == '2':
            while True:
                name = input("Enter member's name: ").strip()
                if name:
                    break
                print("Member name cannot be empty.")
            while True:
                membership_id = input("Enter membership ID: ").strip()
                if membership_id:
                    break
                print("Membership ID cannot be empty.")
            member = Member(name, membership_id)
            library.register_member(member)

        elif choice == '3':
            name = input("Enter member's name: ").strip()
            member = next((m for m in library.members if m.name == name), None)
            if member:
                title = input("Enter the book title you want to borrow: ").strip()
                book = next((b for b in library.books if b.title == title), None)
                if book:
                    member.borrow_book(book)
                else:
                    print("Book not found in the library.")
            else:
                print("Member not found.")

        elif choice == '4':
            name = input("Enter member's name: ").strip()
            member = next((m for m in library.members if m.name == name), None)
            if member:
                title = input("Enter the book title you want to return: ").strip()
                book = next((b for b in library.books if b.title == title), None)
                if book:
                    member.return_book(book)
                else:
                    print("Book not found in the library.")
            else:
                print("Member not found.")

        elif choice == '5':
            library.list_available_books()

        elif choice == '6':
            library.list_borrowed_books()

        elif choice == '7':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice, please try again.")

# Run the menu-driven program
menu()

 """