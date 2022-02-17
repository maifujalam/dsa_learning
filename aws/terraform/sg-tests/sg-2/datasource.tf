resource "null_resource" "sleep_6" {
  provisioner "local-exec" {
    command = "sleep 1"
  }
}
data "aws_security_group" "get_master-sg" {
  filter {
    name   = "tag:Name"
    values = ["jenkins-default"]
  }
  depends_on = [null_resource.sleep_6]
}
data "aws_security_group" "get_worker-sg" {
  filter {
    name   = "tag:Name"
    values = ["default"]
  }
  depends_on = [null_resource.sleep_6]
}
resource "null_resource" "patch_sg" {
  provisioner "local-exec" {
    command = <<EOT
    ansible-playbook /home/alam/Desktop/Projects/dsa_learning/aws/terraform/sg-tests/sg-2/ansible/patch_sg.yaml --extra-vars \
    "master_sg=${data.aws_security_group.get_master-sg.id} \
    allowed_ports=${jsonencode(var.allowed_ports)}
    worker_sg=${data.aws_security_group.get_worker-sg.id}"
    EOT
  }
}