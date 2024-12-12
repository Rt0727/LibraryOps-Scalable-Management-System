#!/bin/bash

# Define database credentials
DB_HOST="localhost"
DB_PORT="5432"
DB_USERNAME="library_user"
DB_PASSWORD="password"
DB_NAME="library_db"

# Define backup location
BACKUP_DIR="./backups"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Perform database backup
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USERNAME $DB_NAME > $BACKUP_FILE

echo "Backup completed: $BACKUP_FILE"