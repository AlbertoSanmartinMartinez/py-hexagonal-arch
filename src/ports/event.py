"""
Event Port module
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional, Any

T = TypeVar('T')

class EventPort(Generic[T], ABC):
    """Event port interface"""
    
    @abstractmethod
    async def push(self, topic: str, data: Any) -> Optional[T]:
        """..."""
        pass
    
    @abstractmethod
    async def pull(self, topic: str) -> None:
        """..."""
        pass