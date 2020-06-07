# cdt_coding_challenge

[![Build Status](https://travis-ci.com/cdt-challenge-group1/cdt_coding_challenge.svg?branch=master)](https://travis-ci.com/cdt-challenge-group1/cdt_coding_challenge)
![Docker Image CI](https://github.com/cdt-challenge-group1/cdt_coding_challenge/workflows/Docker%20Image%20CI/badge.svg)
[![codecov](https://codecov.io/gh/cdt-challenge-group1/cdt_coding_challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/cdt-challenge-group1/cdt_coding_challenge)


## setup

```
sudo apt install git
git clone https://github.com/sophiefsadler/cdt_coding_challenge
cd cdt_coding_challenge
chmod +x setup.sh && sudo ./setup.sh
```

## docker

```
docker build . --file Dockerfile --tag cdt_coding_challenge_deploy:$(date +%s)
docker run --name "cdt" -p 80:80 -d -t [id from build]
```
