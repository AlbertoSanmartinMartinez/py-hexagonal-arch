# Python Hexagonal Architecture Package

A Python package implementing hexagonal architecture pattern with multi-framework web support.

## Features

- ✅ **Hexagonal Architecture**: Clean separation of concerns with ports and adapters
- ✅ **Multi-Framework Support**: FastAPI, Flask, and Tornado support out of the box
- ✅ **Base Controllers**: Generic CRUD operations with filtering
- ✅ **Repository Pattern**: Abstract data access layer
- ✅ **Event System**: Domain event handling
- ✅ **Caching Layer**: Pluggable caching adapters
- ✅ **Type Safety**: Full type hints support

## Structure

```
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

## Examples

See the `examples/` directory for complete working examples with each framework.

## License

MIT License
