import sqlite3

class Database:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    available INTEGER DEFAULT 1
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER,
                    member_id INTEGER,
                    issue_date TEXT,
                    return_date TEXT,
                    FOREIGN KEY (book_id) REFERENCES books (id),
                    FOREIGN KEY (member_id) REFERENCES members (id)
                )
            """)

    def add_book(self, title, author):
        with self.conn:
            self.conn.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

    def add_member(self, name):
        with self.conn:
            self.conn.execute("INSERT INTO members (name) VALUES (?)", (name,))

    def issue_book(self, book_id, member_id):
        with self.conn:
            self.conn.execute("INSERT INTO transactions (book_id, member_id, issue_date) VALUES (?, ?, DATE('now'))", 
                              (book_id, member_id))
            self.conn.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))

    def return_book(self, book_id):
        with self.conn:
            self.conn.execute("UPDATE transactions SET return_date = DATE('now') WHERE book_id = ? AND return_date IS NULL", 
                              (book_id,))
            self.conn.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))