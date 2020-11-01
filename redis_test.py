import redis
from time import sleep

r = redis.Redis(host='172.25.112.1', port=7001)

print(r.ping())

r.set('test100', '100')
r.set('test-ttl', 'ttl', px=10000)

r.hset('Objekt', 'Nimi', 'Juku')
r.hset('Objekt', 'Age', '10')
r.hset('Objekt', 'Price', '100')

r.sadd('testlist', 'test1', 'test2', 'sadd3', 'sadd4')

print(r.get('test100'))
print(r.get('test-ttl'))
print(r.get('test-none'))

sleep(2)

print(r.ttl('test-ttl'))
print(r.ttl('test'))
