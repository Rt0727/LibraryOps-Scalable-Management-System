provider "postgresql" {
  host     = var.db_host
  port     = var.db_port
  username = var.db_username
  password = var.db_password
  database = var.db_name
}

resource "postgresql_database" "library_db" {
  name = var.db_name
}

resource "postgresql_role" "library_user" {
  name     = var.db_username
  password = var.db_password
  login    = true
}

resource "postgresql_grant" "library_db_permissions" {
  role       = postgresql_role.library_user.name
  database   = postgresql_database.library_db.name
  privileges = ["ALL"]
}