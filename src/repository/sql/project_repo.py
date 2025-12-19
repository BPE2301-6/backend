import uuid

from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Project
from src.core.utils import map_model
from src.schemas.dtos import ProjectDTO

from ..interfaces import BaseRepository


class ProjectRepositoryImpl(BaseRepository[Project]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> ProjectDTO | None:
        item = await Project.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, ProjectDTO)

    async def create(self, data: dict) -> ProjectDTO:
        item = Project.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ProjectDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> ProjectDTO | None:
        item = await Project.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ProjectDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Project.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[ProjectDTO]:
        items = await Project.get_all(self.session)
        return [map_model(i, ProjectDTO) for i in items]

    async def get_key_by_id(self, project_id: uuid.UUID) -> str | None:
        stmt = select(Project.key).where(Project.id == project_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_list(
        self, search: str | None, limit: int, offset: int
    ) -> tuple[list[ProjectDTO], int]:
        stmt = select(Project)
        if search:
            stmt = stmt.where(
                or_(Project.name.ilike(f"%{search}%"), Project.key.ilike(f"%{search}%"))
            )
        stmt = stmt.offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        dto_items = [map_model(i, ProjectDTO) for i in items]

        count_stmt = select(func.count()).select_from(Project)
        if search:
            count_stmt = count_stmt.where(
                or_(Project.name.ilike(f"%{search}%"), Project.key.ilike(f"%{search}%"))
            )
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return dto_items, total
