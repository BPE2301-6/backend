import uuid

from src.core.db.models import Status
from ..base import BaseRepository


class StatusRepositoryImpl(BaseRepository[Status]):
    async def get_by_id(self, status_id: uuid.UUID) -> Status | None:
        return await self._db_get(Status, status_id)

    async def create(self, data: dict) -> Status:
        item = Status(**data)
        return await self._db_add(item)

    async def update(self, status_id: uuid.UUID, data: dict) -> Status:
        item = await self._db_get(Status, status_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, status_id: uuid.UUID) -> None:
        item = await self._db_get(Status, status_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_project(self, project_id: uuid.UUID) -> list[Status]:
        return await self._db_list_by(Status, project_id=project_id)
