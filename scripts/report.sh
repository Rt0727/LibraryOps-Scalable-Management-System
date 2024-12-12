#!/bin/bash

# Define database connection parameters
DB_HOST="localhost"
DB_PORT="5432"
DB_USERNAME="library_user"
DB_PASSWORD="password"
DB_NAME="library_db"

# Query to generate overdue books report
OVERDUE_QUERY="SELECT * FROM books WHERE due_date < NOW() AND returned_date IS NULL;"

# Query to generate fines report
FINES_QUERY="SELECT * FROM members WHERE fine > 0;"

# Generate overdue books report
echo "Generating overdue books report..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USERNAME -d $DB_NAME -c "$OVERDUE_QUERY" > overdue_books_report.txt

# Generate fines report
echo "Generating fines report..."
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USERNAME -d $DB_NAME -c "$FINES_QUERY" > fines_report.txt

echo "Reports generated: overdue_books_report.txt, fines_report.txt"