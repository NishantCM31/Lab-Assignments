from datetime import datetime

# Initialize variables for tracking
books_data = []
available_books = 0
checked_out_books = 0
most_borrowed_books = {}
overdue_books = []

# Define today's date for overdue checks
today_date = datetime.now().strftime("%Y-%m-%d")

# Function to validate date format
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to accept a new book's data with validation
def accept_book_data():
    global available_books, checked_out_books, most_borrowed_books, overdue_books
    
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    
    # Validate checked-out status
    while True:
        checked_out = input("Is the book checked out? (yes/no): ").lower()
        if checked_out in ['yes', 'no']:
            checked_out = checked_out == 'yes'
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Validate due date (if provided)
    while True:
        due_date = input("Enter due date (YYYY-MM-DD) or press Enter if not applicable: ")
        if not due_date:
            due_date = None
            break
        elif is_valid_date(due_date):
            break
        else:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    book = {"title": title, "author": author, "checked_out": checked_out, "due_date": due_date}
    books_data.append(book)
    
    # Count available and checked-out books
    if not checked_out:
        available_books += 1
    else:
        checked_out_books += 1

        # Track most borrowed books (based on occurrences in this simple implementation)
        if title in most_borrowed_books:
            most_borrowed_books[title] += 1
        else:
            most_borrowed_books[title] = 1

        # Check if the book is overdue
        if due_date and due_date < today_date:
            overdue_books.append(title)

# Function to display library statistics
def display_statistics():
    global books_data, available_books, checked_out_books, most_borrowed_books, overdue_books

    total_books = len(books_data)
    most_borrowed_book = max(most_borrowed_books, key=most_borrowed_books.get) if most_borrowed_books else "None"

    print(f"\nTotal Books in Library: {total_books}")
    print(f"Available Books: {available_books}")
    print(f"Checked-Out Books: {checked_out_books}")
    print(f"Most Borrowed Book: {most_borrowed_book}")

    print("\nOverdue Books:")
    if overdue_books:
        for book in overdue_books:
            print(f"- {book}")
    else:
        print("None")

# Function to list all books in the library
def list_books():
    if not books_data:
        print("No books in the library.")
    else:
        print("\nBooks in Library:")
        for book in books_data:
            checked_out_status = "Checked Out" if book["checked_out"] else "Available"
            due_date = book["due_date"] if book["due_date"] else "N/A"
            print(f"Title: {book['title']}, Author: {book['author']}, Status: {checked_out_status}, Due Date: {due_date}")

# Function to check for overdue books
def check_overdue_books():
    print("\nOverdue Books:")
    overdue_books_today = [book["title"] for book in books_data if book["checked_out"] and book["due_date"] and book["due_date"] < today_date]
    if overdue_books_today:
        for book in overdue_books_today:
            print(f"- {book}")
    else:
        print("None")

# Function to validate the menu choice
def get_menu_choice():
    while True:
        try:
            choice = int(input("\n--- Library Menu ---\n1. Add a Book\n2. View Library Statistics\n3. List All Books\n4. Check Overdue Books\n5. Exit\nEnter your choice: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main menu-driven interface
def main_menu():
    while True:
        choice = get_menu_choice()

        if choice == 1:
            accept_book_data()
        elif choice == 2:
            display_statistics()
        elif choice == 3:
            list_books()
        elif choice == 4:
            check_overdue_books()
        elif choice == 5:
            print("Exiting the system.")
            break

# Run the main menu
if __name__ == "__main__":
    main_menu()
