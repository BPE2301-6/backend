import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from src.core.db.models import Tag

from ..interfaces import BaseRepository


class TagRepositoryImpl(BaseRepository[Tag]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> Tag | None:
        return await Tag.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> Tag:
        item = Tag.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: uuid.UUID, data: dict) -> Tag | None:
        item = await Tag.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Tag.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[Tag]:
        return await Tag.get_all(self.session)

    async def get_all_by_project(
        self, project_id: uuid.UUID, limit: int, offset: int
    ) -> tuple[list[Tag], int]:
        stmt = select(Tag).where(Tag.project_id == project_id).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_stmt = select(func.count()).select_from(Tag).where(Tag.project_id == project_id)
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return items, total
