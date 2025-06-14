import mysql.connector

# Connect to MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Replace with your username
        password="Rasnaana12@",   # Replace with your password
        database="library_db"
    )

# Add a new book to the database
def add_book(title, author, isbn):
    db = connect()
    cursor = db.cursor()
    query = "INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)"
    values = (title, author, isbn)
    cursor.execute(query, values)
    db.commit()
    print("Book added successfully!")
    cursor.close()
    db.close()

# Search for a book by title
def search_book_by_title(title):
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM books WHERE title LIKE %s"
    cursor.execute(query, ("%" + title + "%",))
    results = cursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print("No books found with that title.")
    cursor.close()
    db.close()

# List all books
def list_all_books():
    db = connect()
    cursor = db.cursor()
    query = "SELECT * FROM books"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print("No books in the library.")
    cursor.close()
    db.close()

# Delete a book by ID
def delete_book_by_id(book_id):
    db = connect()
    cursor = db.cursor()
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
    db.commit()
    if cursor.rowcount:
        print(f"Book with ID {book_id} deleted successfully.")
    else:
        print("No book found with that ID.")
    cursor.close()
    db.close()
