# Python Hexagonal Architecture Package

A Python package implementing hexagonal architecture pattern with multi-framework web support.

## Features

- ✅ **Hexagonal Architecture**: Clean separation of concerns with ports and adapters
- ✅ **Multi-Framework Support**: FastAPI, Flask, and Tornado support out of the box
- ✅ **Base Controllers**: Generic CRUD operations with filtering
- ✅ **Repository Pattern**: Abstract data access layer
- ✅ **Event System**: Domain event handling
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

## Examples

See the `examples/` directory for complete working examples with each framework and caching system.

- `fastapi_example.py` - FastAPI implementation
- `flask_example.py` - Flask implementation  
- `tornado_example.py` - Tornado implementation
- `cache_example.py` - Comprehensive caching examples

## License

MIT License
