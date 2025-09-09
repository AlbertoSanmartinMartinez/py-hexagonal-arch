"""
User Cache module
"""

from typing import TYPE_CHECKING

from adapters.caches.base import BaseCache
from models.user import User


if TYPE_CHECKING:
    pass


class UserCache(BaseCache):
    """..."""

    def __init__(self):
        """..."""

        super().__init__(
            model=User
        )