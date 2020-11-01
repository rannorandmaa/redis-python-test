## run redis

$ docker run -d --rm --name my-redis -p 7001:6379 redis


## run cli

Replace your local host, example is wsl 2 windows.
$ docker run -it --rm --name my-redis-cli redis redis-cli -h 172.25.112.1 -p 7001


## run redis commander

$ docker run --rm --name my-redis-commander -d -p 8081:8081 rediscommander/redis-commander


## python

$ pip install redis
$ pyhton redis_test.py
