from aioredis import from_url

from src.config import CacheSettings

settings = CacheSettings()


async def get_redis():
    redis_pool = await from_url(
        settings.cache_connection_url,
        password=settings.cache_password,
    )
    yield redis_pool
    redis_pool.close()
    await redis_pool.wait_closed()
