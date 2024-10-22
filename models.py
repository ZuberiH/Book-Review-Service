import sqlite3

def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    # Create the books table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
    """)

    # Create the reviews table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        review TEXT NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
    )
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect("books.db")
    conn.row_factory = sqlite3.Row  # Allows dict-like access to rows
    return conn
