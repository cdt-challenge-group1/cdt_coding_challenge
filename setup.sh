#!/bin/bash

sudo apt -y install apache2 php python3 python3-pip &&
sudo cp 100-cdt_coding_challenge.conf /etc/apache2/sites-available &&
sudo a2dissite 000-default &&
sudo a2ensite 100-cdt_coding_challenge &&
sudo service apache2 restart &&
sudo mkdir -p /var/www/html/cdt/ &&
cp -R . /var/www/html/cdt/ &&
sudo chown -R www-data:www-data /var/www &&
sudo pip3 install -r model/requirements.txt &&
wget -O /dev/null -o /dev/null 127.0.0.1 2>&1 /dev/null
