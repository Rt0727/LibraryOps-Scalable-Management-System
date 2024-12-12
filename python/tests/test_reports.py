import unittest
import sqlite3
from database import Database
from reports import ReportGenerator

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        # Initialize an in-memory SQLite database
        self.db = Database(":memory:")
        self.report_generator = ReportGenerator(self.db)

        # Populate test data
        with self.db.conn:
            self.db.conn.execute("INSERT INTO books (title, author, available) VALUES ('Book1', 'Author1', 1)")
            self.db.conn.execute("INSERT INTO members (name) VALUES ('Member1')")
            self.db.conn.execute("INSERT INTO transactions (book_id, member_id, issue_date) VALUES (1, 1, DATE('now', '-15 days'))")

    def test_generate_overdue_report(self):
        # Generate the overdue report
        self.report_generator.generate_overdue_report()

        # Read the generated report file
        with open("overdue_report.txt", "r") as file:
            report_content = file.read()

        # Assert report content
        self.assertIn("Book: Book1", report_content)
        self.assertIn("Member: Member1", report_content)

if __name__ == "__main__":
    unittest.main()