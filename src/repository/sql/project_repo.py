import uuid

from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Project

from ..interfaces import BaseRepository


class ProjectRepositoryImpl(BaseRepository[Project]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> Project | None:
        return await Project.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> Project:
        item = Project.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: uuid.UUID, data: dict) -> Project | None:
        item = await Project.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Project.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[Project]:
        return await Project.get_all(self.session)

    async def get_list(
        self, search: str | None, limit: int, offset: int
    ) -> tuple[list[Project], int]:
        stmt = select(Project)
        if search:
            stmt = stmt.where(
                or_(Project.name.ilike(f"%{search}%"), Project.key.ilike(f"%{search}%"))
            )
        stmt = stmt.offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_stmt = select(func.count()).select_from(Project)
        if search:
            count_stmt = count_stmt.where(
                or_(Project.name.ilike(f"%{search}%"), Project.key.ilike(f"%{search}%"))
            )
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return items, total
