data "aws_vpc" "get_vpc" {
#  filter {
#    name   = "tag:Name"
#    values = [var.ocp_cluster_vpc_name]
#  }
    tags = {
    Name = var.vpc_name
  }
}
data "aws_subnet" "get_subnet" {
  filter {
    name   = "tag:Name"
    values = [var.subnet_name]
  }
}
data "template_file" "host_template" {
  template = <<EOF
[server]

%{ for ip in aws_instance.vm[*].public_ip ~}
${ip} ${"\n"}
%{ endfor ~}

[all:vars]
ansible_user=${var.ssh_user[var.instance_os]}
ansible_ssh_private_key_file=${var.private_key_path}
ansible_ssh_common_args='-o StrictHostKeyChecking=no'
$ansible_python_interpreter=/bin/python3
EOF
}