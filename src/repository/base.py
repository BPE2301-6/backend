from typing import Type, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

T = TypeVar("T")


class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _db_get(self, model: Type[T], id) -> T | None:
        return await self.session.get(model, id)
    
    async def _db_add(self, obj: T) -> T:
        self.session.add(obj)
        await self.session.flush()
        return obj

    async def _db_update(self, obj: T, data: dict) -> T:
        for key, value in data.items():
            setattr(obj, key, value)
        await self.session.flush()
        return obj
    
    async def _db_delete(self, obj: T) -> None:
        await self.session.delete(obj)
        await self.session.flush()

    async def _db_list_all(self, model: Type[T]) -> list[T]:
        result = await self.session.execute(select(model))
        return result.scalars().all()

    async def _db_list_by(self, model: Type[T], **kwargs) -> list[T]:
        stmt = select(model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return result.scalars().all()
