FROM ubuntu
EXPOSE 80

RUN apt-get update && \
      apt-get -y install sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker
RUN echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections

RUN sudo mkdir /source
COPY / /source
COPY setup.sh /setup.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN sudo chmod +x /setup.sh
RUN sudo chmod +x /docker-entrypoint.sh
RUN sudo bash -c 'cd /source && bash /setup.sh'
RUN sudo apt install cron
RUN sudo sh -c "echo '0 0 * * * wget -O /dev/null -o /dev/null localhost' >> /etc/crontab"

#CMD sudo service apache2 start
#CMD wget -O /dev/null -o /dev/null localhost

ENTRYPOINT ["sudo", "/docker-entrypoint.sh"]
CMD ["apache"]
