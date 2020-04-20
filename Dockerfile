FROM ubuntu
EXPOSE 80/tcp

RUN apt-get update && \
      apt-get -y install sudo

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker
RUN echo 'debconf debconf/frontend select Noninteractive' | sudo debconf-set-selections

CMD mkdir /source
COPY / /source
COPY setup.sh /setup.sh
CMD chmod +x /setup.sh
RUN sudo bash -c 'cd /source && bash /setup.sh'
