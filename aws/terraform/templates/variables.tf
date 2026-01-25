variable "region" {
  description = "Region Name"
  type        = string
  default     = "us-east-1"
}
variable "ip_v4" {
  description = "Your IP v4 address"
  type        = string
  default     = "1o.0.0.0/32"
  sensitive = True
  validation {
    condition     = can(regex("^([0-9]{1,3}\\.){3}[0-9]{1,3}/[0-9]{1,2}$", var.ip_v4))
    error_message = "The IP address must be in CIDR notation (e.g.,)
  }
}
variable "image_ami" {
  description = "dd"
  type=string
  default = "ami-0c55b159cbfafe1f0"
  validation {
    condition = length(var.image_ami) > 0 && substring(var.image_ami, 0, 4) == "ami-"
    error_message = "The AMI ID must start with 'ami-' and cannot be empty
  }
}