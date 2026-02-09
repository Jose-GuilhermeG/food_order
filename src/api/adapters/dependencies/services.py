from typing import Annotated

from fastapi import Depends

from api.adapters.cache import RedisCache
from api.application.interfaces.cache import ICache
from api.infra.redis import RedisDep


def get_redis_cache(redis : RedisDep)->ICache:
    return RedisCache(redis)

CacheDep = Annotated[ICache , Depends(get_redis_cache)]
