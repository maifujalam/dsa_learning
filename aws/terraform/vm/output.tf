output "public-ip" {
  value = aws_instance.vm[*].public_ip
}
output "all_ssh_cmd" {
#  value = "ssh -o ServerAliveInterval=5 -i ~/.ssh/id_rsa ${var.ssh_user[var.instance_os]}@${aws_instance.vm[0].public_ip}"
  value = aws_instance.vm[*].public_ip
}
