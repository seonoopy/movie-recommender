#! /bin/zsh


docker rm redis

docker run -d --name redis -p 6379:6379 redis