import argparse
from database import Database
from reports import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Library Management CLI")
    parser.add_argument("--action", choices=["add_book", "add_member", "issue_book", "return_book", "generate_report"],
                        required=True, help="Action to perform in the library system")
    args = parser.parse_args()

    db = Database()

    if args.action == "add_book":
        title = input("Enter book title: ")
        author = input("Enter author: ")
        db.add_book(title, author)
        print("Book added successfully.")
    
    elif args.action == "add_member":
        name = input("Enter member name: ")
        db.add_member(name)
        print("Member added successfully.")
    
    elif args.action == "issue_book":
        book_id = int(input("Enter book ID: "))
        member_id = int(input("Enter member ID: "))
        db.issue_book(book_id, member_id)
        print("Book issued successfully.")
    
    elif args.action == "return_book":
        book_id = int(input("Enter book ID: "))
        db.return_book(book_id)
        print("Book returned successfully.")
    
    elif args.action == "generate_report":
        report = ReportGenerator(db)
        report.generate_overdue_report()
        print("Overdue report generated successfully.")

if __name__ == "__main__":
    main()