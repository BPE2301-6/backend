from typing import Any, Tuple
from uuid import UUID

from ..interfaces import BaseService
from src.repository import Store


class TaskTagServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: Tuple[UUID, UUID]) -> Any | None:
        item = await self.store.task_tag_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.task_tag_repo().create(data)
        return item

    async def update(self, item_id: Tuple[UUID, UUID], data: dict) -> Any:
        item = await self.store.task_tag_repo().update(item_id, data)
        return item

    async def delete(self, item_id: Tuple[UUID, UUID]) -> None:
        await self.store.task_tag_repo().delete(item_id)

    async def get_all(self) -> list[Any]:
        items = await self.store.task_tag_repo().get_all()
        return items
