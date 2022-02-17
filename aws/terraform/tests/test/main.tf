resource "aws_security_group_rule" "add_master_sg-IPIP" {
  type              = "ingress"
  from_port         = 4
  to_port           = 4
  protocol          = "tcp"
  security_group_id = ""
  source_security_group_id = ""
}
#resource "aws_security_group_rule" "add_worker_sg-IPIP" {
#  type              = "ingress"
#  from_port         = 4
#  to_port           = 4
#  protocol          = "tcp"
#  security_group_id = data.aws_security_group.get_master-sg.id
#  source_security_group_id = data.aws_security_group.get_worker-sg.id
#}