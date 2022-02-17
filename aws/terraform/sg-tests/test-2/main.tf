
resource "null_resource" "example" {
  provisioner "local-exec" {
    command = "echo hello >${path.module}/hello.txt"
  }
}

data "local_file" "example" {
  filename = "${path.module}/machoine-set.yaml"
  depends_on = ["null_resource.example"]
}

output "aaa" {
  value = yamldecode(data.local_file.example.content)["metadata"]["labels"]["machine.openshift.io/cluster-api-cluster"]
}