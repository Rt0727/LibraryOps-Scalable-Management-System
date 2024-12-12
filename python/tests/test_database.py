import unittest
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")

    def test_add_book(self):
        self.db.add_book("Test Book", "Test Author")
        books = self.db.conn.execute("SELECT * FROM books").fetchall()
        self.assertEqual(len(books), 1)

if __name__ == "__main__":
    unittest.main()
