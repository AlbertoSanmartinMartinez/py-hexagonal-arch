"""
Base Event module
"""

from typing import TypeVar, Generic, Optional, Any, Type
import json

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from ports.event import EventPort
from config.settings import settings

T = TypeVar('T')


class BaseEvent(EventPort[T], Generic[T]):
    """Base event class"""

    def __init__(
        self,
        model: Type[T],
    ):
        """..."""

        self.model = model

    def _get_producer(self):
        
        def value_serializer(v: Any) -> bytes:
            if hasattr(v, 'model_dump'):
                return json.dumps(v.model_dump(), default=str).encode('utf-8')
            return json.dumps(v, default=str).encode('utf-8')
        
        def key_serializer(k: Any) -> bytes | None:
            if k is None:
                return None
            if hasattr(k, 'model_dump'):
                return json.dumps(k.model_dump(), default=str).encode('utf-8')
            return json.dumps(k, default=str).encode('utf-8')
        
        return AIOKafkaProducer(
            bootstrap_servers=settings.kafka_server,
            value_serializer=value_serializer,
            key_serializer=key_serializer
        )

    def _get_consumer(self):
        
        return AIOKafkaConsumer(
            bootstrap_servers=settings.kafka_server,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')) if v else None,
            key_deserializer=lambda k: json.loads(k.decode('utf-8')) if k else None
        )
    
    async def push(self, topic: str, data: Any) -> None:
        """..."""

        producer = self._get_producer()
        await producer.start()
        
        await producer.send_and_wait(
            f"{self.model.__name__}.{topic}",
            data
        )
    
    async def pull(self, topic: str) -> None:
        """..."""

        consumer = self._get_consumer()
        await consumer.start()