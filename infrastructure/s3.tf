resource "aws_s3_bucket" "dl" {
  bucket = "datalake-brx-edc-tf"
  acl    = "private"

  tags = {
    IES   = "BRONXHOME",
    CURSO = "EDC"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }
}