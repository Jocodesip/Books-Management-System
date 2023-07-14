import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

# Create
def create_book(title, author, year):
    cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    conn.commit()
    print("Book created successfully!")

# Read
def read_books():
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    if rows:
        print("Books:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}")
    else:
        print("No books found.")

# Update
def update_book(book_id, title, author, year):
    cursor.execute('UPDATE books SET title=?, author=?, year=? WHERE id=?', (title, author, year, book_id))
    conn.commit()
    print("Book updated successfully!")

# Delete
def delete_book(book_id):
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()
    print("Book deleted successfully!")

def display_menu():
    print("\n----- Book Management System -----")
    print("1. Create a new book")
    print("2. Read all books")
    print("3. Update a book")
    print("4. Delete a book")
    print("0. Exit")

def get_user_choice():
    choice = input("Enter your choice (0-4): ")
    return int(choice)

def get_book_details():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = int(input("Enter the publication year: "))
    return title, author, year

def get_book_id():
    book_id = int(input("Enter the book ID: "))
    return book_id

# CLI loop
while True:
    display_menu()
    choice = get_user_choice()

    if choice == 1:
        title, author, year = get_book_details()
        create_book(title, author, year)
    elif choice == 2:
        read_books()
    elif choice == 3:
        book_id = get_book_id()
        title, author, year = get_book_details()
        update_book(book_id, title, author, year)
    elif choice == 4:
        book_id = get_book_id()
        delete_book(book_id)
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

