import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import TaskTag
from src.core.utils import map_model
from src.schemas.dtos import TaskTagDTO

from ..interfaces import BaseRepository


class TaskTagRepositoryImpl(BaseRepository[TaskTag]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> TaskTagDTO | None:
        item = await TaskTag.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, TaskTagDTO)

    async def create(self, data: dict) -> TaskTagDTO:
        item = TaskTag.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskTagDTO)

    async def update(self, item_id: tuple[uuid.UUID, uuid.UUID], data: dict) -> TaskTagDTO | None:
        item = await TaskTag.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskTagDTO)

    async def delete(self, item_id: tuple[uuid.UUID, uuid.UUID]) -> None:
        item = await TaskTag.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[TaskTagDTO]:
        items = await TaskTag.get_all(self.session)
        return [map_model(i, TaskTagDTO) for i in items]
