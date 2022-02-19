locals {
  ports = var.ingress_ports
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
  ami                         = var.ami.ubuntu-20
  instance_type               = var.instance_type
  tags                        = {
    Name = "${var.instance_name}-${count.index+1}"
    owner= "alam"
    oc = var.instance_os
  }
  key_name                    = var.instance_key
  subnet_id                   = data.aws_subnet.get_subnet.id
  vpc_security_group_ids      = [aws_security_group.sg.id]
  associate_public_ip_address = true
  availability_zone = var.zone
  root_block_device {
    volume_size = var.root_volume_size
    delete_on_termination = true
  }
  provisioner "remote-exec" {
    inline = [
      "echo server provisioned.",
      #"sudo apt update -y"
    ]

  }
  connection {
    type = "ssh"
    user = var.ssh_user[var.instance_os]
    password = ""
    private_key = file(var.private_key_path)
    host = self.public_ip
  }
  lifecycle {
    ignore_changes = [ami,security_groups]
  }
}
resource "local_file" "ansible" {
  content = data.template_file.host_template.rendered
  filename = "${path.cwd}/ansible/hosts"
  provisioner "local-exec" {
    command= <<EOF
             ansible-playbook ${path.cwd}/ansible/install_nginx.yaml -i ${path.cwd}/ansible/hosts
    EOF
  }
}