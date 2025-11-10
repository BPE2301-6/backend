import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import TaskTag
from ..interfaces import BaseRepository


class TaskTagRepositoryImpl(BaseRepository[TaskTag]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> TaskTag | None:
        return await TaskTag.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> TaskTag:
        item = TaskTag.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: tuple[uuid.UUID, uuid.UUID], data: dict) -> TaskTag | None:
        item = await TaskTag.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> None:
        item = await TaskTag.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[TaskTag]:
        return await TaskTag.get_all(self.session)
