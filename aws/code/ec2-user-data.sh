#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html


## Ubuntu
#      apt update
#      apt -y install apache2
#      cat <<EOF > /var/www/html/index.html
#      <html><body><p>Linux startup script added directly.</p></body></html>'