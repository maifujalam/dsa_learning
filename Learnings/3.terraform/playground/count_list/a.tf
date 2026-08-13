terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "3.2.4"
    }
  }
}
resource "null_resource" "abc" {
  dynamic "abcd" {
    for_each = tolist(["one", "two", "three"])
    content {
        value = abcd.key
      keys = abcd.value
    }
  }
}