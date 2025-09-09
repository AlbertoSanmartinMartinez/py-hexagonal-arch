"""
User Repository module
"""

from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from adapters.repositories.base import BaseRepository, BaseSchema
from models.user import User
from schemas.user import UserSchema
from config.databases import engine


class UserRepository(BaseRepository[User]):
    """Repository for handling User model operations"""
    
    def __init__(self):
        """..."""

        super().__init__(
            model=User,
            schema=UserSchema
        )
