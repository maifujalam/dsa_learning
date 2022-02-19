data "aws_vpc" "get_vpc" {
  filter {
    name   = "tag:Name"
    values = [var.vpc_name]
  }
}
data "aws_security_group" "get-sg" {
  filter {
    name   = "tag:Name"
    values = ["nexus-sg"]
  }
}
#data "aws_security_groups" "get_master-sg" {
#  filter {
#    name   = "tag:Name"
#    values = ["cluster-1-6ksqr-master-sg"]
#  }
#}