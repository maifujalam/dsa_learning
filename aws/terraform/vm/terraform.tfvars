region = "us-east-1"
zone = "us-east-1a"
instance_name = "vm-ubuntu"
instance_os = "ubuntu"  # it will be ubuntu or rhel
instance_type = "t2.micro"
root_volume_size = 10
instance_count = 2
ingress_ports = [22,80,443,8080]
vpc_name = "vpc-1"
subnet_name = "public-subnet-1"
security_group = "lb-sg-1"
instance_key = "vm-key"
public_key_path = "~/.ssh/aws/key.pub"
private_key_path = "~/.ssh/aws/key"
enable_public_ip = true
