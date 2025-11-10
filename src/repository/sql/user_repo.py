import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import User

from ..interfaces import BaseRepository


class UserRepositoryImpl(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> User | None:
        return await User.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> User:
        item = User.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: uuid.UUID, data: dict) -> User | None:
        item = await User.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await User.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[User]:
        return await User.get_all(self.session)
