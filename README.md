# Python Hexagonal Architecture Package

A Python package implementing hexagonal architecture pattern with multi-framework web support.

## Features

- ✅ **Hexagonal Architecture**: Clean separation of concerns with ports and adapters
- ✅ **Multi-Framework Support**: FastAPI, Flask, and Tornado support out of the box
- ✅ **Base Controllers**: Generic CRUD operations with filtering
- ✅ **Multi-Database Support**: PostgreSQL, MariaDB, SQL Server, Oracle
- ✅ **Multi-Messaging Support**: Kafka, RabbitMQ, AWS Kinesis, GCP Pub/Sub
- ✅ **Multi-Cache Support**: Redis, MemCache, and In-Memory caching
- ✅ **Type Safety**: Full type hints support

## Structure

```bash
src/
├── adapters/           # External adapters (web, db, cache, etc.)
│   ├── routers/       # Web framework routers
│   ├── repositories/  # Data access implementations
│   ├── caches/        # Cache implementations
│   └── events/        # Event handlers
├── controllers/        # Application controllers
├── models/            # Domain models
├── ports/             # Application ports (interfaces)
├── schemas/           # Data schemas
└── config/            # Configuration
```

## Quick Start

### 1. Install Dependencies

```bash
# For FastAPI
pip install fastapi uvicorn pydantic

# For Flask
pip install flask pydantic

# For Tornado
pip install tornado pydantic

# For Redis caching
pip install redis

# For MemCache caching
pip install aiomcache

# For Kafka messaging
pip install aiokafka

# For RabbitMQ messaging
pip install aio-pika

# For AWS Kinesis
pip install aioboto3

# For Google Cloud Pub/Sub
pip install google-cloud-pubsub

# For PostgreSQL (default)
pip install asyncpg

# For MariaDB/MySQL
pip install aiomysql

# For SQL Server
pip install aioodbc

# For Oracle
pip install cx_oracle_async
```

### 2. Create a Model

```python
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    age: int
```

### 3. Create a Controller

```python
from controllers.base import BaseController

class UserController(BaseController[User]):
    # Implement your business logic
    pass
```

### 4. Set Up Repository

```python
from adapters.repositories.user import UserRepository

# PostgreSQL (default)
user_repo = UserRepository()

# MariaDB/MySQL
user_repo = UserRepository(db_type="mariadb")

# SQL Server
user_repo = UserRepository(db_type="sqlserver")

# Oracle
user_repo = UserRepository(db_type="oracle")

# Basic operations
user = User(name="John", email="john@example.com")
created_user = await user_repo.create(user)
users = await user_repo.list()
```

📖 **For detailed repository documentation, configuration, and advanced usage, see: [`src/adapters/repositories/README.md`](src/adapters/repositories/README.md)**

### 5. Create a Router

```python
from adapters.routers.base import BaseRouter

# FastAPI (default)
user_router = BaseRouter(
    model=User,
    controller=UserController,
    prefix="/users",
    tags=["users"]
)

# Flask
user_router = BaseRouter(
    model=User,
    controller=UserController,
    prefix="/users",
    tags=["users"],
    framework="flask"
)

# Tornado
user_router = BaseRouter(
    model=User,
    controller=UserController,
    prefix="/users",
    tags=["users"],
    framework="tornado"
)
```

📖 **For detailed router documentation, patterns, and advanced usage, see: [`src/adapters/routers/README.md`](src/adapters/routers/README.md)**

### 6. Set Up Caching

```python
from adapters.caches.user import UserCache

# Redis (default)
user_cache = UserCache()

# MemCache
user_cache = UserCache(
    cache_type="memcache",
    servers=["localhost:11211"]
)

# In-Memory (for testing)
user_cache = UserCache(cache_type="memory")

# Usage
user = User(id="1", name="John", email="john@example.com", age=30)
await user_cache.set("user:1", user)
cached_user = await user_cache.get("user:1")
```

📖 **For detailed cache documentation, patterns, and advanced usage, see: [`src/adapters/caches/README.md`](src/adapters/caches/README.md)**

### 7. Set Up Events

```python
from adapters.events.user import UserEvent

# Kafka (default)
user_events = UserEvent()

# RabbitMQ
user_events = UserEvent(event_type="rabbitmq")

# AWS Kinesis
user_events = UserEvent(event_type="kinesis")

# Basic operations
await user_events.push("created", user, key=user.id)
async for user_data in user_events.pull("created"):
    print(f"User event: {user_data.name}")
```

📖 **For detailed event documentation, patterns, and advanced usage, see: [`src/adapters/events/README.md`](src/adapters/events/README.md)**

## Examples

See the `examples/` directory for complete working examples with each framework and caching system.

- `fastapi_example.py` - FastAPI implementation
- `flask_example.py` - Flask implementation  
- `tornado_example.py` - Tornado implementation
- `repositories_example.py` - Multi-database repository examples
- `cache_example.py` - Comprehensive caching examples
- `events_example.py` - Multi-backend event messaging examples

## License

MIT License
