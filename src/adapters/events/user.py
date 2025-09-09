"""
User Event module
"""

from typing import TYPE_CHECKING

from adapters.events.base import BaseEvent
from models.user import User


if TYPE_CHECKING:
    pass


class UserEvent(BaseEvent):
    """..."""

    def __init__(self):
        """..."""

        super().__init__(
            model=User
        )