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

# Event Messaging Configuration
EVENT_TYPE = os.environ.get("EVENT_TYPE", "kafka")  # kafka, rabbitmq, kinesis, pubsub, memory

# Kafka
KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "localhost:9092")
#print(KAFKA_SERVER)

# RabbitMQ
RABBITMQ_URL = os.environ.get("RABBITMQ_URL", "amqp://localhost")

# AWS Kinesis
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

# Google Cloud Pub/Sub
GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "")
GCP_CREDENTIALS_PATH = os.environ.get("GCP_CREDENTIALS_PATH", "")

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

    # Event messaging settings
    event_type: str = EVENT_TYPE
    kafka_server: str = KAFKA_SERVER
    rabbitmq_url: str = RABBITMQ_URL
    
    # AWS settings
    aws_region: str = AWS_REGION
    aws_access_key_id: str = AWS_ACCESS_KEY_ID
    aws_secret_access_key: str = AWS_SECRET_ACCESS_KEY
    
    # GCP settings
    gcp_project_id: str = GCP_PROJECT_ID
    gcp_credentials_path: str = GCP_CREDENTIALS_PATH

    openai_api_key: str = OPENAI_API_KEY
    claude_api_key: str = CLAUDE_API_KEY

settings = Settings()