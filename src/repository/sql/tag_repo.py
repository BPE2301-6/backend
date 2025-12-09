import uuid
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Tag
from src.schemas.dtos import TagDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class TagRepositoryImpl(BaseRepository[Tag]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> TagDTO | None:
        item = await Tag.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, TagDTO)

    async def create(self, data: dict) -> TagDTO:
        item = Tag.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TagDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> TagDTO | None:
        item = await Tag.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TagDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Tag.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[TagDTO]:
        items = await Tag.get_all(self.session)
        return [map_model(i, TagDTO) for i in items]

    async def get_all_by_project(
        self, project_id: uuid.UUID, limit: int, offset: int
    ) -> tuple[list[TagDTO], int]:
        stmt = select(Tag).where(Tag.project_id == project_id).offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        dto_items = [map_model(i, TagDTO) for i in items]

        count_stmt = select(func.count()).select_from(Tag).where(Tag.project_id == project_id)
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return dto_items, total
