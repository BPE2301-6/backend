from typing import Any
from uuid import UUID

from ..interfaces import BaseService
from src.repository import Store


class CommentServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Any | None:
        item = await self.store.comments.get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.comments.create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> Any:
        item = await self.store.comments.update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.comments.delete(item_id)

    async def get_all(self) -> list[Any]:
        items = await self.store.comments.get_all()
        return items
