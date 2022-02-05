locals {
  ports = [22,80,443]
}
resource "aws_key_pair" "key" {
  public_key = file(var.public_key_path)
  key_name   = var.instance_key
  tags = {
    Name = var.instance_key
    owner = "alam"
  }
}
resource "aws_security_group" "sg" {
  name = var.security_group
  vpc_id = data.aws_vpc.get_vpc.id
  dynamic "ingress" {
    for_each = local.ports
    content {
      from_port = ingress.value
      to_port = ingress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  ingress {
    from_port = -1
    protocol  = "ICMP"
    to_port   = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
  dynamic "egress" {
    for_each = local.ports
    content {
      from_port = egress.value
      to_port = egress.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
  tags   = {
    Name = var.security_group
    owner = "alam"
  }
}
resource "aws_instance" "vm" {
  count = var.instance_count
  ami                         = var.ami
  instance_type               = var.instance_type
  tags                        = {
    Name = "${var.instance_name}-${count.index}"
    owner= "alam"
  }
  key_name                    = var.instance_key
  subnet_id                   = data.aws_subnet.get_subnet.id
  vpc_security_group_ids      = [aws_security_group.sg.id]
  associate_public_ip_address = "true"
#  lifecycle {
#    ignore_changes = [ami]
#  }
#  availability_zone = var.zone
  root_block_device {
    volume_size = var.root_volume_size
    delete_on_termination = true
  }
  provisioner "remote-exec" {
    inline = [
      #"sudo yum update -y",
      "sudo apt install -y httpd",
      "sudo systemctl start httpd",
      "sudo systemctl enable httpd",
      "echo '<h1>Hello from $(hostname -f)</h1>'  | sudo tee  /var/www/html/index.html"
    ]
  }
  connection {
    type = "ssh"
    user = "ec2-user"
    password = ""
    private_key = file(var.private_key_path)
    host = self.public_ip
  }
}
