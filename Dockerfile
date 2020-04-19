FROM ubuntu
EXPOSE 80/tcp
COPY setup.sh /setup.sh
CMD chmod +x /setup.sh
ENTRYPOINT ["/setup.sh"]
