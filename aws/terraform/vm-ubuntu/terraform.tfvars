region = "us-east-1"
zone = "us-east-1a"
ami = "ami-04505e74c0741db8d"   # rhel-8.5=ami-0b0af3577fe5e3532   ubuntu-20=ami-04505e74c0741db8d
instance_name = "vm"
instance_type = "t2.micro"
vpc_name = "default-vpc"
subnet_name = "default-subnet-1"
security_group = "vm-sg"
instance_key = "vm-key"
public_key_path = "~/.ssh/id_rsa.pub"
private_key_path = "~/.ssh/id_rsa"
root_volume_size = 10
instance_count = 1