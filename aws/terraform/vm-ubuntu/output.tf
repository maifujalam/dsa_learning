output "public-ip" {
  value = aws_instance.vm[*].id
}
output "ssh" {
  value = "ssh -o ServerAliveInterval=5 -i ~/.ssh/id_rsa ec2-user@${aws_instance.vm[0].public_ip}"
}
