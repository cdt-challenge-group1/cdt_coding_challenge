#!/bin/bash

sudo apt -y install apache2 php python3 python3-pip &&
sudo cp 100-cdt_coding_challenge.conf /etc/apache2/sites-available &&
sudo a2dissite 000-default &&
sudo a2ensite 100-cdt_coding_challenge &&
sudo a2enmod deflate &&
sudo service apache2 restart &&
sudo mkdir -p /var/www/html/cdt/ &&
cp -R . /var/www/html/cdt/ &&
sudo chown -R www-data:www-data /var/www &&
sudo pip3 install -r model/requirements.txt &&
sudo python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon
#wget -O /dev/null -o /dev/null 127.0.0.1?run 2>&1 /dev/null
