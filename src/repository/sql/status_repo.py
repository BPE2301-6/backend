import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Status

from ..interfaces import BaseRepository


class StatusRepositoryImpl(BaseRepository[Status]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> Status | None:
        return await Status.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> Status:
        item = Status.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: uuid.UUID, data: dict) -> Status | None:
        item = await Status.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Status.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[Status]:
        return await Status.get_all(self.session)
