from typing import Any
from uuid import UUID

from src.repository import Store

from ..interfaces import BaseService


class ProjectMemberServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: tuple[UUID, UUID]) -> Any | None:
        item = await self.store.project_member_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.project_member_repo().create(data)
        return item

    async def update(self, item_id: tuple[UUID, UUID], data: dict) -> Any:
        item = await self.store.project_member_repo().update(item_id, data)
        return item

    async def delete(self, item_id: tuple[UUID, UUID]) -> None:
        await self.store.project_member_repo().delete(item_id)

    async def get_all(self) -> list[Any]:
        items = await self.store.project_member_repo().get_all()
        return items

    async def get_all_by_project(self, project_id: UUID) -> list[Any]:
        items = await self.store.project_member_repo().get_all_by_project(project_id)
        return items
