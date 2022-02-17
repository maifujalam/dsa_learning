variable "aws_region" {
  description = "AWS region to configure openshift network infrastructure"
}
variable "vpc_name" {
    description = "VPC Name"
}
variable "allowed_ports" {
  type = list(number)
  default = [234,235]
}