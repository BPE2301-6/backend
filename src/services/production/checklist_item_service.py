from uuid import UUID

from src.repository import Store
from src.schemas.dtos import ChecklistItemDTO

from ..interfaces import BaseService


class ChecklistItemServiceImpl(BaseService[ChecklistItemDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> ChecklistItemDTO | None:
        item = await self.store.checklist_item_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> ChecklistItemDTO:
        item = await self.store.checklist_item_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> ChecklistItemDTO:
        item = await self.store.checklist_item_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.checklist_item_repo().delete(item_id)

    async def get_all(self) -> list[ChecklistItemDTO]:
        items = await self.store.checklist_item_repo().get_all()
        return items

    async def get_by_checklist_id(self, checklist_id: UUID) -> list[ChecklistItemDTO]:
        items = await self.store.checklist_item_repo().get_by_checklist_id(checklist_id)
        return items
