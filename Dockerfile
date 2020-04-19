FROM ubuntu
EXPOSE 80/tcp
WORKDIR /home/runner/work/cdt_coding_challenge/cdt_coding_challenge
RUN chmod +x setup.sh
RUN ./setup.sh
