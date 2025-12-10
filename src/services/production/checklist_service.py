<<<<<<< HEAD
=======
from typing import Any
>>>>>>> dev
from uuid import UUID

from src.repository import Store
from src.schemas.dtos import ChecklistDTO

from ..interfaces import BaseService


<<<<<<< HEAD
class ChecklistServiceImpl(BaseService[ChecklistDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> ChecklistDTO | None:
        item = await self.store.checklist_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> ChecklistDTO:
        item = await self.store.checklist_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> ChecklistDTO:
=======
class ChecklistServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Any | None:
        item = await self.store.checklist_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.checklist_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> Any:
>>>>>>> dev
        item = await self.store.checklist_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.checklist_repo().delete(item_id)

<<<<<<< HEAD
    async def get_all(self) -> list[ChecklistDTO]:
        items = await self.store.checklist_repo().get_all()
        return items

    async def get_by_task_id(self, task_id: UUID) -> ChecklistDTO | None:
=======
    async def get_all(self) -> list[Any]:
        items = await self.store.checklist_repo().get_all()
        return items

    async def get_by_task_id(self, task_id: UUID) -> Any | None:
>>>>>>> dev
        item = await self.store.checklist_repo().get_by_task_id(task_id)
        return item
