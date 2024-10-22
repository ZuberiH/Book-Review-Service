from models import get_db_connection

# Function to get all books
def get_all_books():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return books

# Function to get a single book by ID
def get_book_by_id(book_id):
    conn = get_db_connection()
    book = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    return book

# Function to add a new book
def add_new_book(title, author):
    conn = get_db_connection()
    conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

# Function to update a book's details
def update_book(book_id, title, author):
    conn = get_db_connection()
    conn.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (title, author, book_id))
    conn.commit()
    conn.close()

# Function to delete a book
def delete_book(book_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

# Function to add a review for a book
def add_review(book_id, review):
    conn = get_db_connection()
    conn.execute("INSERT INTO reviews (book_id, review) VALUES (?, ?)", (book_id, review))
    conn.commit()
    conn.close()

# Function to get all reviews for a book
def get_reviews(book_id):
    conn = get_db_connection()
    reviews = conn.execute("SELECT * FROM reviews WHERE book_id = ?", (book_id,)).fetchall()
    conn.close()
    return reviews
