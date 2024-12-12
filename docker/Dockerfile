FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

# Copy application files into the container
COPY . /app

# Set the default command to run the CLI application
CMD ["python", "library_management_cli.py"]