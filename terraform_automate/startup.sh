#! bin/bash
apt-get update
apt install nginx -y
systemctl start nginx
systemctl enable nginx
echo "Hello World" > /var/www/html/index.html

