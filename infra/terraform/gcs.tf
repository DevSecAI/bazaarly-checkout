provider "google" { project = "bazaarly-prod", region = "europe-west2" }

resource "google_storage_bucket" "assets" {
  name                        = "bazaarly-assets-prod"
  location                    = "EU"
  uniform_bucket_level_access = true
}

# BAZ-IAC-001: bucket made world-readable.
resource "google_storage_bucket_iam_member" "public" {
  bucket = google_storage_bucket.assets.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
}
