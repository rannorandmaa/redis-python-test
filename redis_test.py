import redis
from redis.sentinel import Sentinel
from time import sleep

sentinel = Sentinel([('1.1.1.1',26379),
                     ('2.1.1.1',26379),
                     ('3.1.1.1',26379)],
                   #sentinel_kwargs={'password': password123}
                   )
host, port = sentinel.discover_master('som-sentinel-dev')
print(f'And the Master is... {host}:{port}')

#r = redis.StrictRedis(host='0.0.0.0', port=6379, password='password123')
r = redis.Redis(host=host, port=port)
#r = redis.Redis(host='0.0.0.0', port=6379)
print(r)

#
# test pub sub
#

ps = r.pubsub()
ps.subscribe('xxx-yyy')

r.publish('xxx-yyy', 'juku message content data text')

msg1 = ps.get_message()
msg1.keys()
print(type(msg1))
print(f'Got message: {msg1}')

msg2 = ps.get_message()
msg2.keys()
print(type(msg2))
print(f'Got message: {msg2}')

#
# just some key value testing
#

print(r.exists("xxxcccvvv"))
print(r.exists("test100"))

print(r.ping())

r.set('test100', '100')
r.set('test-ttl', 'ttl', px=10000)

r.hset('Objekt', 'Nimi', 'Juku')
r.hset('Objekt', 'Age', '10')
r.hset('Objekt', 'Price', '100')

r.sadd('testlist', 'test1', 'test2', 'sadd3', 'sadd4')

print(f"test100 -> {r.get('test100')}")
print(f"test-ttl -> {r.get('test-ttl')}")
print(f"test-none -> {r.get('test-none')}")

sleep(2)

print(f"test-ttl -> {r.ttl('test-ttl')}")
print(f"test -> {r.ttl('test')}")
