#  Check below URL for Further reference of firewall rules:-
# https://docs.openshift.com/container-platform/4.8/installing/installing_aws/installing-aws-vpc.html#installation-custom-aws-vpc-isolation_installing-aws-vpc

resource "aws_security_group_rule" "add_master_sg-170" {
  count = length(var.allowed-ports)
  type              = "ingress"
  from_port         = element(var.allowed-ports,count.index).port
  to_port           = element(var.allowed-ports,count.index).port
  protocol          = element(var.allowed-ports,count.index).protocol
  security_group_id = data.aws_security_group.get-sg.id
  source_security_group_id =data.aws_security_group.get-sg.id
  description = "Manual Port Added"
}