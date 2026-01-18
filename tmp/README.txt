1. This vagrant is for running vm with virtualbox provider on apple mac m1/m2 chip;

# Ruby
BOX_NAME = "bento/ubuntu-24.04"
BOX_VERSION = "202510.26.0"
CPU_COUNT = 2
MEMORY_SIZE = "2048"
NETWORK_IP = "192.168.0.2"
ADDITIONAL_DISK_COUNT = 3
ADDITIONAL_DISK_SIZE = "5GB"

Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: NETWORK_IP ,virtualbox__intnet: "mynetwork"
  config.vm.box_check_update = false
  config.vm.define "server" do |s|
    s.vm.box = BOX_NAME
    s.vm.box_version = BOX_VERSION
    s.vm.provider "virtualbox" do |vb|
      vb.memory = MEMORY_SIZE
      vb.cpus = CPU_COUNT
    end
    (0..ADDITIONAL_DISK_COUNT).each do |i|
        s.vm.disk :disk, size: ADDITIONAL_DISK_SIZE, name: "disk-#{i}"
    end
    s.vm.hostname = "server"
    s.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update && sudo apt-get upgrade -y
      sudo apt-get install -y build-essential git wget curl vim net-tools htop jq unzip software-properties-common apt-transport-https
    SHELL
  end
end

# End of the Vagrantfile
