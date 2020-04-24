# cdt_coding_challenge

## setup

```sudo apt install git
git clone https://github.com/sophiefsadler/cdt_coding_challenge
cd cdt_coding_challenge
chmod +x setup.sh && sudo ./setup.sh
```

## docker

```docker build . --file Dockerfile --tag cdt_coding_challenge_deploy:$(date +%s)
docker run --name "cdt" -p 80:80 -d -t [id from build]
```
