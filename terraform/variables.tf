variable "db_host" {
  description = "The host address for the PostgreSQL database"
  type        = string
}

variable "db_port" {
  description = "The port for PostgreSQL database"
  type        = number
  default     = 5432
}

variable "db_username" {
  description = "The username for the PostgreSQL database"
  type        = string
}

variable "db_password" {
  description = "The password for the PostgreSQL database"
  type        = string
}

variable "db_name" {
  description = "The name of the PostgreSQL database"
  type        = string
}