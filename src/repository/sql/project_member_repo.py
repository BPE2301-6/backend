import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import ProjectMember
from src.schemas.dtos import ProjectMemberDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class ProjectMemberRepositoryImpl(BaseRepository[ProjectMember]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> ProjectMemberDTO | None:
        item = await ProjectMember.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, ProjectMemberDTO)

    async def create(self, data: dict) -> ProjectMemberDTO:
        item = ProjectMember.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ProjectMemberDTO)

    async def update(
        self, item_id: tuple[uuid.UUID, uuid.UUID], data: dict
    ) -> ProjectMemberDTO | None:
        item = await ProjectMember.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ProjectMemberDTO)

    async def delete(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> None:
        item = await ProjectMember.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[ProjectMemberDTO]:
        items = await ProjectMember.get_all(self.session)
        return [map_model(i, ProjectMemberDTO) for i in items]

    async def get_all_by_project(self, project_id: uuid.UUID) -> list[ProjectMemberDTO]:
        stmt = select(ProjectMember).where(ProjectMember.project_id == project_id)
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        return [map_model(i, ProjectMemberDTO) for i in items]
