import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import TaskSequence
from src.core.utils import map_model
from src.schemas.dtos import TaskSequenceDTO

from ..interfaces import BaseRepository


class TaskSequenceRepositoryImpl(BaseRepository[TaskSequence]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> TaskSequenceDTO | None:
        item = await TaskSequence.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, TaskSequenceDTO)

    async def create(self, data: dict) -> TaskSequenceDTO:
        item = TaskSequence.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskSequenceDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> TaskSequenceDTO | None:
        item = await TaskSequence.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, TaskSequenceDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await TaskSequence.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[TaskSequenceDTO]:
        items = await TaskSequence.get_all(self.session)
        return [map_model(i, TaskSequenceDTO) for i in items]
