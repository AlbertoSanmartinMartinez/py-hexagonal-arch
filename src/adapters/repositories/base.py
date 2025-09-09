"""
Base Repository module
"""

from typing import TypeVar, Generic, List, Optional, Type, Any
from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import selectinload

from ports.repository import RepositoryPort, FilterList, FilterCondition
from config.databases import engine
from models.base import CustomModel

T = TypeVar('T', bound=CustomModel)

BaseSchema = declarative_base()


class BaseRepository(RepositoryPort[T], Generic[T]):
    """Base repository class"""
    
    def __init__(
        self,
        model: Type[T],
        schema: Type[T]
    ):
        """..."""

        self.model = model
        self.schema = schema

    def _build_filter_condition(self, filter_condition: FilterCondition) -> Any:
        """Build SQLAlchemy filter condition from FilterCondition"""

        attribute = getattr(self.schema, filter_condition.attribute)
        
        if filter_condition.operator == "eq":
            return attribute == filter_condition.value
        elif filter_condition.operator == "ne":
            return attribute != filter_condition.value
        elif filter_condition.operator == "gt":
            return attribute > filter_condition.value
        elif filter_condition.operator == "gte":
            return attribute >= filter_condition.value
        elif filter_condition.operator == "lt":
            return attribute < filter_condition.value
        elif filter_condition.operator == "lte":
            return attribute <= filter_condition.value
        elif filter_condition.operator == "like":
            return attribute.like(filter_condition.value)
        elif filter_condition.operator == "ilike":
            return attribute.ilike(filter_condition.value)
        elif filter_condition.operator == "in":
            return attribute.in_(filter_condition.value)
        elif filter_condition.operator == "not_in":
            return ~attribute.in_(filter_condition.value)
        else:
            raise ValueError(f"Unsupported operator: {filter_condition.operator}")

    async def create(self, item: T) -> T:
        """Create a new item"""

        async with AsyncSession(engine) as session:

            item_data = item.model_dump(exclude_none=True)
            db_item = self.schema(**item_data)
            session.add(db_item)
            await session.commit()
            await session.refresh(db_item)
            
            return self.model.model_validate(db_item.__dict__)

    async def list(self, filters: Optional[FilterList] = None) -> List[T]:
        """List all items with optional filters"""

        async with AsyncSession(engine) as session:
            
            query = select(self.schema)
            
            if filters:
                filter_conditions = []
                for filter_condition in filters:
                    try:
                        condition = self._build_filter_condition(filter_condition)
                        filter_conditions.append(condition)
                    except (AttributeError, ValueError) as e:
                        print(f"Invalid filter condition: {filter_condition}, error: {e}")
                        continue
                
                if filter_conditions:
                    query = query.where(and_(*filter_conditions))
            
            result = await session.execute(query)
            items = result.scalars().all()
            
            return [self.model.model_validate(item.__dict__) for item in items]

    async def detail(
        self,
        pk: str,
        include_relations: Optional[List[str]] = None
    ) -> Optional[T]:
        """Get item by primary key"""
        
        async with AsyncSession(engine) as session:

            query = select(self.schema).where(
                getattr(self.schema, self.model.pk_field) == pk
            )
            
            if include_relations:
                for relation in include_relations:
                    if hasattr(self.schema, relation):
                        query = query.options(selectinload(getattr(self.schema, relation)))
            
            result = await session.execute(query)
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            return self.model.model_validate(item.__dict__)

    async def update(self, pk: str, item_update: T) -> T:
        """Update an item"""
        
        async with AsyncSession(engine) as session:

            result = await session.execute(
                select(self.schema).where(
                    getattr(self.schema, self.model.pk_field) == pk
                )
            )
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            item_data = item_update.model_dump(exclude_unset=True)
            for key, value in item_data.items():
                setattr(item, key, value)
            
            session.add(item)
            await session.commit()
            await session.refresh(item)
            
            return self.model.model_validate(item.__dict__)

    async def delete(self, pk: str) -> None:
        """Delete an item"""
        
        async with AsyncSession(engine) as session:
            result = await session.execute(
                select(self.schema).where(
                    getattr(self.schema, self.model.pk_field) == pk
                )
            )
            item = result.scalar_one_or_none()
            
            if not item:
                raise HTTPException(
                    status_code=404,
                    detail=f"{self.model.__name__} with pk: {pk} not found"
                )
            
            await session.delete(item)
            await session.commit()
