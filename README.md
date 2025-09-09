# Python Hexagonal Architecture Package

A Python package implementing hexagonal architecture pattern with multi-framework web support.

## Features

- ✅ **Hexagonal Architecture**: Clean separation of concerns with ports and adapters
- ✅ **Multi-Framework Support**: FastAPI, Flask, and Tornado support out of the box
- ✅ **Base Controllers**: Generic CRUD operations with filtering
- ✅ **Repository Pattern**: Abstract data access layer
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

### 4. Create a Router

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

### 5. Set Up Caching

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

### 6. Set Up Events

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

## Event System

The package includes a flexible multi-backend event messaging system:

### Supported Backends
- **Apache Kafka**: High-throughput distributed streaming
- **RabbitMQ**: Reliable message broker with advanced routing
- **AWS Kinesis**: Real-time data streaming service
- **Google Cloud Pub/Sub**: Global messaging and ingestion
- **In-Memory**: Fast events for testing and development

### Basic Usage

```python
from adapters.events.user import UserEvent

# Kafka (default)
user_events = UserEvent()

# RabbitMQ
user_events = UserEvent(event_type="rabbitmq")

# AWS Kinesis
user_events = UserEvent(
    event_type="kinesis",
    region_name="us-east-1"
)

# Publish events
await user_events.push("created", user, key=user.id)

# Subscribe to events
async for user_data in user_events.pull("created"):
    print(f"Processing: {user_data.name}")
```

📖 **For detailed event documentation, patterns, and advanced usage, see: [`src/adapters/events/README.md`](src/adapters/events/README.md)**

## Examples

See the `examples/` directory for complete working examples with each framework and caching system.

- `fastapi_example.py` - FastAPI implementation
- `flask_example.py` - Flask implementation  
- `tornado_example.py` - Tornado implementation
- `cache_example.py` - Comprehensive caching examples
- `events_example.py` - Multi-backend event messaging examples

## License

MIT License
