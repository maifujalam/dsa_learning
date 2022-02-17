resource "null_resource" "approve_csr" {
  provisioner "local-exec" {
    command= <<EOF
             ansible-playbook ${path.cwd}/ansible/approve_csr.yaml -i ${path.cwd}/ansible/hosts  --extra-vars install_complete_flag=${path.cwd}/setup_complete
    EOF
  }
}
resource "null_resource" "wait_cluster_create" {
  provisioner "local-exec" {
    command = <<EOF
    sleep 30
    #touch ${path.cwd}/setup_complete
    EOF
  }
}