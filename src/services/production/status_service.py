from uuid import UUID

from src.repository import Store
from src.schemas.dtos import StatusDTO

from ..interfaces import BaseService


class StatusServiceImpl(BaseService[StatusDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> StatusDTO | None:
        item = await self.store.status_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> StatusDTO:
        item = await self.store.status_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> StatusDTO:
        item = await self.store.status_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.status_repo().delete(item_id)

    async def get_all(self) -> list[StatusDTO]:
        items = await self.store.status_repo().get_all()
        return items

    async def get_all_by_project(self, project_id: UUID) -> list[StatusDTO]:
        items = await self.store.status_repo().get_all_by_project(project_id)
        return items
