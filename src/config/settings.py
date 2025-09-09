"""
Settings module
"""

import os
from typing import List


# General
ENVIRONMENT = os.environ.get("ENVIRONMENT", "")
VERSION = os.environ.get("VERSION", "")

# Postgres
POSTGRES_NAME = os.environ.get("POSTGRES_NAME")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
#print(POSTGRES_URL)

# Redis
REDIS_PROTOCOL = os.environ.get("REDIS_PROTOCOL")
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_USER = os.environ.get("REDIS_USER")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_TTL = int(os.environ.get("REDIS_TTL", 3600))
REDIS_URL: str = f"{REDIS_PROTOCOL}://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
#print(REDIS_URL)

# Cache Configuration
CACHE_TYPE = os.environ.get("CACHE_TYPE", "redis")  # redis, memcache, memory
CACHE_TTL = int(os.environ.get("CACHE_TTL", REDIS_TTL))

# MemCache
MEMCACHE_SERVERS = os.environ.get("MEMCACHE_SERVERS", "127.0.0.1:11211").split(",")
MEMCACHE_TTL = int(os.environ.get("MEMCACHE_TTL", 3600))

# Kafka
KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "")
#print(KAFKA_SERVER)

# OpenAI
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
CLAUDE_API_KEY = os.environ.get("CLAUDE_API_KEY", "")


class Settings:
    """..."""

    environment: str = ENVIRONMENT
    version: str = VERSION

    postgres_url: str = POSTGRES_URL
    
    redis_url: str = REDIS_URL
    redis_ttl: int = REDIS_TTL
    
    # Cache settings
    cache_type: str = CACHE_TYPE
    cache_ttl: int = CACHE_TTL
    
    # MemCache settings
    memcache_servers: List[str] = MEMCACHE_SERVERS
    memcache_ttl: int = MEMCACHE_TTL

    kafka_server: str = KAFKA_SERVER

    openai_api_key: str = OPENAI_API_KEY
    claude_api_key: str = CLAUDE_API_KEY

settings = Settings()