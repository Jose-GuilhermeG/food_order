from typing import Annotated

from fastapi import Depends
from redis import Redis

from api.infra.settings import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


def get_redis():
    redis = Redis(
        decode_responses=True,
        host=REDIS_HOST,
        password=REDIS_PASSWORD,
        port=REDIS_PORT,
        username="default",
        db=0
    )


    yield redis

RedisDep = Annotated[Redis , Depends(get_redis)]
