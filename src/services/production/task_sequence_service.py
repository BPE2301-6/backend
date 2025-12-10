from uuid import UUID

from src.repository import Store
from src.schemas.dtos import TaskSequenceDTO

from ..interfaces import BaseService


class TaskSequenceServiceImpl(BaseService[TaskSequenceDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> TaskSequenceDTO | None:
        item = await self.store.task_sequence_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> TaskSequenceDTO:
        item = await self.store.task_sequence_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> TaskSequenceDTO:
        item = await self.store.task_sequence_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_sequence_repo().delete(item_id)

    async def get_all(self) -> list[TaskSequenceDTO]:
        items = await self.store.task_sequence_repo().get_all()
        return items
