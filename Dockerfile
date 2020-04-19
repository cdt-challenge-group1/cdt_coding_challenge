FROM ubuntu
EXPOSE 80/tcp
WORKDIR /root
COPY dockerimage/setup.sh setup.sh
RUN chmod +x setup.sh
RUN ./setup.sh
