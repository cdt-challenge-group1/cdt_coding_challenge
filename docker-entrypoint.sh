#!/bin/bash
set -e

if [ "$1" = 'apache' ]; then
        echo "Starting Apache"
        # https://github.com/docker-library/httpd/blob/master/2.4/httpd-foreground
		rm -f /usr/local/apache2/logs/httpd.pid

		export APACHE_RUN_DIR=/etc/apache2/
		export APACHE_RUN_USER=www-data
		export APACHE_RUN_GROUP=www-data
		export APACHE_LOG_DIR=/var/log/apache2/
		#exec httpd -DFOREGROUND "$@"
		exec apache2 -DFOREGROUND
		#-e debug
fi

exec "$@"
