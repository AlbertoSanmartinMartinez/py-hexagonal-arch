"""
Base Cache module
"""

from typing import TypeVar, Generic, Optional, Type
from redis.asyncio import from_url
from pydantic import BaseModel

from ports.cache import CachePort
from config.settings import settings

T = TypeVar('T', bound=BaseModel)


class BaseCache(CachePort[T], Generic[T]):
    """Base cache class"""
    
    model: type[T]

    def __init__(
        self,
        model: Type[T]
    ):
        """..."""

        self.model = model
        self.async_redis_client = from_url(
            url=settings.redis_url,
            encoding="UTF-8",
            decode_responses=True
        )

    async def get(self, key: str) -> Optional[T]:
        """Get item from cache"""

        data: str = await self.async_redis_client.get(key)
        
        if data:
            return self.model.model_validate_json(data)
        
        return None

    async def set(self, key: str, data: T) -> None:
        """Set item in cache"""

        await self.async_redis_client.set(
            key,
            data.model_dump_json(),
            ex=settings.redis_ttl
        )

    async def delete(self, key: str) -> None:
        """Delete item from cache"""

        await self.async_redis_client.delete(key)