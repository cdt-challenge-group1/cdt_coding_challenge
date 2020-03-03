#!/bin/bash

sudo apt install apache2 &&
sudo apt install php &&
sudo cp 100-cdt_coding_challenge.conf /etc/apache2/sites-available &&
sudo a2dissite 000-default &&
sudo a2ensite 100-cdt_coding_challenge &&
sudo service apache2 restart &&
sudo mkdir -p /var/www/html/cdt/ &&
cp -R . /var/www/html/cdt/ &&
sudo chown -R www-data:www-data /var/www
