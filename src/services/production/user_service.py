<<<<<<< HEAD
=======
from typing import Any
>>>>>>> dev
from uuid import UUID

from src.repository import Store
from src.schemas.dtos import UserDTO

from ..interfaces import BaseService


<<<<<<< HEAD
class UserServiceImpl(BaseService[UserDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> UserDTO | None:
        item = await self.store.user_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> UserDTO:
        item = await self.store.user_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> UserDTO:
=======
class UserServiceImpl(BaseService[Any]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> Any | None:
        item = await self.store.user_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> Any:
        item = await self.store.user_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> Any:
>>>>>>> dev
        item = await self.store.user_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.user_repo().delete(item_id)

<<<<<<< HEAD
    async def get_all(self) -> list[UserDTO]:
        items = await self.store.user_repo().get_all()
        return items

    async def get_list(self, search: str, limit: int, offset: int) -> tuple[list[UserDTO], int]:
=======
    async def get_all(self) -> list[Any]:
        items = await self.store.user_repo().get_all()
        return items

    async def get_list(self, search: str, limit: int, offset: int) -> tuple[list[Any], int]:
>>>>>>> dev
        items, total = await self.store.user_repo().get_list(search, limit, offset)
        return items, total
