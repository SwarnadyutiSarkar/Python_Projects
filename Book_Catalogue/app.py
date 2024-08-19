import sqlite3
import pandas as pd

# Initialize SQLite database
def initialize_db():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    # Create books table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL,
        genre TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

# Add a new book
def add_book(title, author, isbn, genre):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO books (title, author, isbn, genre) VALUES (?, ?, ?, ?)
    ''', (title, author, isbn, genre))
    
    conn.commit()
    conn.close()

# Display all books
def display_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Genre: {book[4]}")
    
    conn.close()

# Search books by title
def search_by_title(title):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM books WHERE title LIKE ?', (f"%{title}%",))
    books = cursor.fetchall()
    
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}, Genre: {book[4]}")
    
    conn.close()

# Update book details
def update_book(id, title, author, isbn, genre):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE books SET title=?, author=?, isbn=?, genre=? WHERE id=?
    ''', (title, author, isbn, genre, id))
    
    conn.commit()
    conn.close()

# Delete a book
def delete_book(id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM books WHERE id=?', (id,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    
    while True:
        print("\nBook Catalogue")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search by Title")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            genre = input("Enter book genre: ")
            add_book(title, author, isbn, genre)
        
        elif choice == '2':
            display_books()
        
        elif choice == '3':
            title = input("Enter title to search: ")
            search_by_title(title)
        
        elif choice == '4':
            id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            isbn = input("Enter new ISBN: ")
            genre = input("Enter new genre: ")
            update_book(id, title, author, isbn, genre)
        
        elif choice == '5':
            id = int(input("Enter book ID to delete: "))
            delete_book(id)
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")
