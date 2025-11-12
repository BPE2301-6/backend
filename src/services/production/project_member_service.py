from typing import Any, Tuple
from uuid import UUID

from ..interfaces import BaseService
from src.repository import Store


class ProjectMemberServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: Tuple[UUID, UUID]) -> Any | None:
        item = await self.store.project_members.get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.project_members.create(data)
        return item

    async def update(self, item_id: Tuple[UUID, UUID], data: dict) -> Any:
        item = await self.store.project_members.update(item_id, data)
        return item

    async def delete(self, item_id: Tuple[UUID, UUID]) -> None:
        await self.store.project_members.delete(item_id)

    async def get_all(self) -> list[Any]:
        items = await self.store.project_members.get_all()
        return items
