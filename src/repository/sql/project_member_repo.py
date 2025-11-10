import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import ProjectMember

from ..interfaces import BaseRepository


class ProjectMemberRepositoryImpl(BaseRepository[ProjectMember]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> ProjectMember | None:
        return await ProjectMember.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> ProjectMember:
        item = ProjectMember.from_dict(data)
        return await item.save(self.session)

    async def update(
        self, item_id: tuple[uuid.UUID, uuid.UUID], data: dict
    ) -> ProjectMember | None:
        item = await ProjectMember.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> None:
        item = await ProjectMember.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[ProjectMember]:
        return await ProjectMember.get_all(self.session)
