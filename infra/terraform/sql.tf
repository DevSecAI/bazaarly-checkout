resource "google_sql_database_instance" "bazaarly" {
  name             = "bazaarly-prod"
  database_version = "POSTGRES_15"
  region           = "europe-west2"

  settings {
    tier = "db-custom-2-4096"

    ip_configuration {
      ipv4_enabled = true
      # BAZ-IAC-002: open to the world.
      authorized_networks {
        name  = "all"
        value = "0.0.0.0/0"
      }
      # BAZ-IAC-003: SSL not required.
      require_ssl = false
    }
  }
}
