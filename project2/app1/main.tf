terraform {
  backend "gcs" {
    bucket  = "tf-state-prod"
    prefix  = "project2/app2"
  }
}
