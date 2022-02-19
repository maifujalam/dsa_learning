variable "region" {
  description = "Region Name"
}
variable "ami" {
  description = "AMI"
  type        = map(string)
  default     = {
    "rhel-8"    = "ami-0b0af3577fe5e3532"
    "ubuntu-20" = "ami-04505e74c0741db8d"
  }
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
  default     = 1
  type        = number
  description = "No of Instances"
}
variable "private_key_path" {
  description = "Private Key path"
  default     = "~/.ssh/id_rsa"
}
variable "ssh_user" {
  type    = map(string)
  default = {
    "ubuntu" = "ubuntu"
    "rhel"   = "ec2-user"
  }
}
variable "ingress_ports" {
  type    = list(number)
  default = [22, 80, 443]
}
variable "instance_os" {
  type = string
  default = "rhel"
}
variable "enable_public_ip" {
  default = "true"
  description = "Whether to provide Public IP t"
}