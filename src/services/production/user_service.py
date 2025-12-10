from uuid import UUID

from src.repository import Store
from src.schemas.dtos import UserDTO

from ..interfaces import BaseService


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
        item = await self.store.user_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.user_repo().delete(item_id)

    async def get_all(self) -> list[UserDTO]:
        items = await self.store.user_repo().get_all()
        return items

    async def get_list(self, search: str, limit: int, offset: int) -> tuple[list[UserDTO], int]:
        items, total = await self.store.user_repo().get_list(search, limit, offset)
        return items, total
