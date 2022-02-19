output "public-ip" {
  value = aws_instance.vm[*].public_ip
}
output "all_ssh_cmd" {
  value = [for i in aws_instance.vm[*]: format("ssh -o ServerAliveInterval=5 -i ~/.ssh/aws/key ${var.ssh_user[var.instance_os]}@%s",i.public_ip)]
}
