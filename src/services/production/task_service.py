from typing import Any
from uuid import UUID

from src.repository import Store

from ..interfaces import BaseService


class TaskServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Any | None:
        item = await self.store.task_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.task_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> Any:
        item = await self.store.task_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_repo().delete(item_id)

    async def get_all(self) -> list[Any]:
        items = await self.store.task_repo().get_all()
        return items

    async def get_all_by_project(
        self, project_id: UUID, filters: dict, limit: int, offset: int, sort: str
    ) -> tuple[list[Any], int]:
        items, total = await self.store.task_repo().get_all_by_project(
            project_id, filters, limit, offset, sort
        )
        return items, total
