variable "aws_region" {
  description = "AWS region to configure openshift network infrastructure"
}
variable "vpc_name" {
    description = "VPC Name"
}
variable "allowed-ports" {
  type = list(map(any))
  default = [
    {"port":"179","protocol":"tcp"},
    {"port":"4","protocol":"4"},
  ]
}