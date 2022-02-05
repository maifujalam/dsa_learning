
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo hello >${path.module}/hello.txt"
  }
}

data "local_file" "example" {
  filename = "${path.module}/metadata.json"
  depends_on = ["null_resource.example"]
}

output "aaa" {
  value = jsondecode(data.local_file.example.content)["infraID"]
}