<<<<<<< HEAD
=======
from typing import Any
>>>>>>> dev
from uuid import UUID

from src.repository import Store
from src.schemas.dtos import TaskDTO

from ..interfaces import BaseService


<<<<<<< HEAD
class TaskServiceImpl(BaseService[TaskDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> TaskDTO | None:
        item = await self.store.task_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> TaskDTO:
        item = await self.store.task_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> TaskDTO:
=======
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
>>>>>>> dev
        item = await self.store.task_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_repo().delete(item_id)

<<<<<<< HEAD
    async def get_all(self) -> list[TaskDTO]:
=======
    async def get_all(self) -> list[Any]:
>>>>>>> dev
        items = await self.store.task_repo().get_all()
        return items

    async def get_all_by_project(
        self, project_id: UUID, filters: dict, limit: int, offset: int, sort: str
<<<<<<< HEAD
    ) -> tuple[list[TaskDTO], int]:
=======
    ) -> tuple[list[Any], int]:
>>>>>>> dev
        items, total = await self.store.task_repo().get_all_by_project(
            project_id, filters, limit, offset, sort
        )
        return items, total
