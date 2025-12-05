from uuid import UUID
from typing import Optional

from src.repository import Store

from ..interfaces import BaseService


class TaskServiceImpl(BaseService[...]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Optional[...]:
        item = await self.store.task_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> ...:
        item = await self.store.task_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> ...:
        item = await self.store.task_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_repo().delete(item_id)

    async def get_all(self) -> list[...]:
        items = await self.store.task_repo().get_all()
        return items
    
    async def get_all_by_project(
        self,
        project_id: UUID,
        filters: dict,
        limit: int,
        offset: int,
        sort: str
    ) -> tuple[list[dict], int]:
        return [], 0
