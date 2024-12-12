class ReportGenerator:
    def __init__(self, db):
        self.db = db

    def generate_overdue_report(self):
        with self.db.conn as conn:
            result = conn.execute("""
                SELECT 
                    b.title AS book_title,
                    m.name AS member_name,
                    t.issue_date,
                    t.return_date
                FROM transactions t
                JOIN books b ON t.book_id = b.id
                JOIN members m ON t.member_id = m.id
                WHERE t.return_date IS NULL AND DATE('now') > DATE(t.issue_date, '+14 days')
            """)
            with open("overdue_report.txt", "w") as file:
                for row in result:
                    file.write(f"Book: {row['book_title']}, Member: {row['member_name']}, Issue Date: {row['issue_date']}\n")