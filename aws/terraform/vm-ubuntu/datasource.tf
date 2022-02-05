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
