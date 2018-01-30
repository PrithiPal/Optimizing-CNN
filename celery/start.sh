#!/bin/bash


## close previous and start new redis server.
echo -e '--------[ closing previous redis-server] -----------'
pgrep 'redis-server' | xargs -n1 -I {} kill -9 {}

## run new redis server
echo -e '--------[ redis-server : starting new ] ------------'
redis-server --daemonize yes

## set password to redis-server

echo -e '--------[ redis-server : setting new pass ] --------'
PASSWORD='babaji'
echo "CONFIG SET requirepass $PASSWORD" | redis-cli


## starting flower
echo -e '--------[ flower-server : starting new ] -----------'
flower -A tasks --port=5555 &

## starting celery server
echo -e '--------[ celery-server : setting new ] ------------'
&celery -A tasks worker --loglevel=info -f celery.log
