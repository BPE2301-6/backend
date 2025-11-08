import uuid

from src.core.db.models import User
from ..base import BaseRepository


class UserRepositoryImpl(BaseRepository[User]):
    async def get_by_id(self, user_id: uuid.UUID) -> User | None:
        return await self._db_get(User, user_id)

    async def create(self, data: dict) -> User:
        item = User(**data)
        return await self._db_add(item)

    async def update(self, user_id: uuid.UUID, data: dict) -> User:
        item = await self._db_get(User, user_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, user_id: uuid.UUID) -> None:
        item = await self._db_get(User, user_id)
        if item is not None:
            await self._db_delete(item)

    async def list_all(self) -> list[User]:
        return await self._db_list_all(User)
