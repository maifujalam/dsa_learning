#  Check below URL for Further reference of firewall rules:-
# https://docs.openshift.com/container-platform/4.8/installing/installing_aws/installing-aws-vpc.html#installation-custom-aws-vpc-isolation_installing-aws-vpc

locals {
  ports = [22,6443]
}
/*
resource "aws_security_group" "bastion-vm-sg" {
  name = "cluster-1-b4l88-master-sg"
  vpc_id = data.aws_vpc.get_vpc.id
#  dynamic "ingress" {
#    for_each = local.ports
#    content {
#      from_port = ingress.value
#      to_port = ingress.value
#      protocol = "tcp"
#      cidr_blocks = ["0.0.0.0/0"]
#    }
#  }
  ingress {
    from_port = -1
    protocol  = "ICMP"
    to_port   = -1
    cidr_blocks = ["0.0.0.0/0"]
  }
#  dynamic "egress" {
#    for_each = local.ports
#    content {
#      from_port = egress.value
#      to_port = egress.value
#      protocol = "tcp"
#      cidr_blocks = ["0.0.0.0/0"]
#    }
#  }
#  egress {
#    from_port = -1
#    protocol  = "ICMP"
#    to_port   = -1
#    cidr_blocks = ["0.0.0.0/0"]
#  }
#  tags   = {
#    Name = "bastion-sg"
#  }

*/
resource "aws_security_group_rule" "add_master_sg-170" {
  count = data.aws_security_group.get_master-sg.filter.values == [179] ? 0  : 1
  type              = "ingress"
  from_port         = 179
  to_port           = 179
  protocol          = "tcp"
  security_group_id = data.aws_security_group.get_master-sg.id
  source_security_group_id = data.aws_security_group.get_master-sg.id

}