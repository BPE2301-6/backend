<<<<<<< HEAD
=======
from typing import Any
>>>>>>> dev
from uuid import UUID

from src.repository import Store
from src.schemas.dtos import CommentDTO

from ..interfaces import BaseService


<<<<<<< HEAD
class CommentServiceImpl(BaseService[CommentDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> CommentDTO | None:
        item = await self.store.comment_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> CommentDTO:
        item = await self.store.comment_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> CommentDTO:
=======
class CommentServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Any | None:
        item = await self.store.comment_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.comment_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> Any:
>>>>>>> dev
        item = await self.store.comment_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.comment_repo().delete(item_id)

<<<<<<< HEAD
    async def get_all(self) -> list[CommentDTO]:
=======
    async def get_all(self) -> list[Any]:
>>>>>>> dev
        items = await self.store.comment_repo().get_all()
        return items

    async def get_all_by_task(
        self, task_id: UUID, limit: int, offset: int
<<<<<<< HEAD
    ) -> tuple[list[CommentDTO], int]:
=======
    ) -> tuple[list[Any], int]:
>>>>>>> dev
        items, total = await self.store.comment_repo().get_all_by_task(task_id, limit, offset)
        return items, total
