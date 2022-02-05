variable "region" {
  description= "Region Name"
}
variable "zone" {
  description = "Zone name"
}
variable "ami" {
  description = "AMI"
}
variable "instance_type" {
  description = "VM Type"
}
variable "instance_name" {
  description = "VM Name"
}
variable "instance_key" {
  description = "VM Key"
}
variable "vpc_name" {
  description = "VPC Name"
}
variable "subnet_name" {
  description = "Subnet Name"
}
variable "public_key_path" {
  description = ""
}
variable "root_volume_size" {
  description = "Size of root volume"
}
variable "security_group" {
  description = ""
}
variable "instance_count" {
  default = 1
  type = number
  description = "No of Instances"
}
variable "private_key_path" {
  description = "Private Key path"
  default = "~/.ssh/id_rsa"
}