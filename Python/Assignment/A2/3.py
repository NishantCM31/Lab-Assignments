# Problem 3:
# Library Management System

# Background:
# A small community library needs a system to manage its book collection and track book checkouts. The system should allow the library to store information about books, track which books are checked out, and provide summaries such as the total number of books available, the most borrowed books, and overdue books.

# Objective:

# Create a Python program that manages a library's book collection, tracks checkouts, and provides insights into the library's usage.

# Book Data Format:
# The book data is stored in a list oi dictionaries, where each dictionary contains:
# 'title": The title of the book (string).
# 'author": The author ot the book (string).
# "checked_out": Boolean value indicating whether the  book is curcently checked out.
# "due_date": The due date for the book (if checked out) as a string in the format YYYY-MM-DD

from datetime import datetime

# Sample Book Data
books_data = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "checked_out": True, "due_date": "2024-08-15"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "checked_out": False, "due_date": None},
    {"title": "1984", "author": "George Orwell", "checked_out": True, "due_date": "2024-08-10"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "checked_out": True, "due_date": "2024-08-21"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "checked_out": False, "due_date": None},
    {"title": "Moby-Dick", "author": "Herman Melville", "checked_out": True, "due_date": "2024-08-05"},
]

# Initialize variables for tracking
total_books = len(books_data)
available_books = 0
checked_out_books = 0
most_borrowed_books = {}
overdue_books = []

# Define today's date for overdue checks
today_date = datetime.now().strftime("%Y-%m-%d")

# Process the library data
for book in books_data:
    title = book["title"]
    checked_out = book["checked_out"]
    due_date = book["due_date"]
    
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

# Find the most borrowed book (book with the highest count in the dictionary)
most_borrowed_book = max(most_borrowed_books, key=most_borrowed_books.get) if most_borrowed_books else "None"

# Display the results
print(f"Total Books in Library: {total_books}")
print(f"Available Books: {available_books}")
print(f"Checked-Out Books: {checked_out_books}")
print(f"Most Borrowed Book: {most_borrowed_book}")

print("\nOverdue Books:")
if overdue_books:
    for book in overdue_books:
        print(f"- {book}")
else:
    print("None")
