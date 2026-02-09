from redis import Redis

from api.application.interfaces.cache import ICache


class RedisCache(ICache):
    def __init__(self , redis : Redis):
        self.redis = redis

    def set_cache(self , key, value):
        self.redis.set(key , "test")

    def get_cache(self, key):
        return self.redis.get(key)
