# coding: utf-8

import json
import redis


REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0


class Manager(object):
    def __init__(self):
        self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def set(self, key, value, expire_at=None):
        self.redis.set(key, json.dumps(value))
        if expire_at is not None:
            self.redis.expireat(key, int(expire_at))

    def get(self, key):
        value = self.redis.get(key)
        try:
            return json.loads(value)
        except TypeError:
            return value


manager = Manager()
