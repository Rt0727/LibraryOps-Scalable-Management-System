# Library Management System with Reporting and CLI Interface (Setup)

## 📚 Overview
This project provides a comprehensive setup for a Library Management System using PostgreSQL, Docker, and Terraform. It includes a Command-Line Interface (CLI) tool for managing library operations such as handling books, members, and transactions. Additionally, the project features automation scripts for generating overdue and fine reports and performing database backups.

## 💡 Key Features
- **PostgreSQL Database**: Stores all library data including books, members, and transactions.
- **Docker Containers**: Ensures consistency and portability across environments.
- **Terraform IaC**: Automates the provisioning of database resources.
- **Bash Scripts**: Simplifies routine tasks like backups and report generation.
- **CLI Interface**: Provides a user-friendly way to interact with the library system.
- **Python Integration**: Core logic for managing the library and running unit tests.

---

## 🛠️ Technologies Used

| Technology        | Purpose                               |
|-------------------|---------------------------------------|
| **PostgreSQL**    | Database for library data            |
| **Docker**        | Containerization                     |
| **Terraform**     | Infrastructure provisioning          |
| **Bash Scripts**  | Automation of routine tasks          |
| **Python**        | Core application logic for the CLI   |

---

## 🚀 Getting Started

### Prerequisites
- Install [Docker](https://www.docker.com/get-started)
- Install [Terraform](https://developer.hashicorp.com/terraform/downloads)
- Install [Python 3.8+](https://www.python.org/downloads/)
- Clone the repository

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rt0727/LibraryOps-Scalable-Management-System.git
cd LibraryOps-Scalable-Management-System
```

### 2️⃣ Configure Terraform
Create a `.tfvars` file in the `terraform/` directory with the following configuration:
```hcl
db_host     = "localhost"
db_port     = 5432
db_username = "library_user"
db_password = "password"
db_name     = "library_db"
```

### 3️⃣ Initialize and Deploy Infrastructure
Navigate to the `terraform/` directory:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```

### 4️⃣ Build and Start Docker Containers
Return to the root directory and build the Docker containers:
```bash
docker-compose up --build
```

### 5️⃣ Run the CLI Tool
Interact with the Library Management System using the CLI tool:
```bash
docker-compose exec app python library_management_cli.py
```

---

## 🛡️ Maintenance

### 1️⃣ Backup the Database
Run the database backup script:
```bash
./scripts/backup.sh
```

### 2️⃣ Generate Reports
Automate overdue and fine report generation:
```bash
./scripts/generate_report.sh
```

---

## 📝 Project Structure
```
library-management-system-setup/
│
├── terraform/
│   ├── main.tf                    # Define PostgreSQL database and resources
│   ├── variables.tf               # Define variables for setup (e.g., db credentials)
│   └── outputs.tf                 # Output values (e.g., database URL)
│
├── docker/
│   ├── Dockerfile                 # Dockerfile for CLI app
│   └── docker-compose.yml         # Docker Compose for local setup
│
├── python/
│   ├── app/
│   │   ├── library_management_cli.py  # CLI for library operations
│   │   ├── database.py               # Database connection and queries
│   │   ├── reports.py                # Report generation logic
│   │   ├── utils.py                  # Utility functions
│   │   └── __init__.py               # Python package init file
│   └── tests/
│       ├── test_database.py           # Unit tests for report generation
│       ├── test_utils.py             # Unit tests for utility functions
│       └── test_reports.py            # Python package init file
│
├── scripts/
│   ├── backup.sh                  # Automated database backup script
│   └── generate_report.sh         # Script to generate overdue and fine reports
│
├── README.md                      # Documentation on setup, instructions
└── .gitignore                     # Git ignore file
```

---

## 🔧 Troubleshooting

### Common Issues
1. **Docker container not starting**:
   - Ensure Docker Desktop is running.
   - Check if the ports defined in `docker-compose.yml` are not in use.
2. **Terraform errors**:
   - Ensure the correct `variables.tfvars` file is used.
   - Run `terraform plan` to identify issues before applying changes.
3. **CLI tool issues**:
   - Verify the Python environment and required libraries are installed.

---

## 📬 Contact
For questions or suggestions, feel free to contact me at:
📧 [rt07mahifan@gmail.com](mailto:rt07mahifan@gmail.com)

---

## 🏆 Acknowledgments
Special thanks to the open-source community for providing tools and resources that made this project possible.

