terraform {
  backend "gcs" {
    bucket  = "tf-state-prod"
    prefix  = "project1/app1"
  }
}
