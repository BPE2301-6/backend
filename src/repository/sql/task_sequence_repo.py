import uuid

from src.core.db.models import TaskSequence
from ..base import BaseRepository


class TaskSequenceRepositoryImpl(BaseRepository[TaskSequence]):
    async def get_by_project(self, project_id: uuid.UUID) -> TaskSequence | None:
        return await self._db_get(TaskSequence, project_id)

    async def create(self, data: dict) -> TaskSequence:
        item = TaskSequence(**data)
        return await self._db_add(item)

    async def update_by_project(self, project_id: uuid.UUID, data: dict) -> TaskSequence | None:
        item = await self._db_get(TaskSequence, project_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete_by_project(self, project_id: uuid.UUID) -> None:
        item = await self._db_get(TaskSequence, project_id)
        if item:
            await self._db_delete(item)
