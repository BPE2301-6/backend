import uuid

from src.core.db.models import TaskTag
from ..base import BaseRepository


class TaskTagRepositoryImpl(BaseRepository[TaskTag]):
    async def get(self, task_id: uuid.UUID, tag_id: uuid.UUID) -> TaskTag | None:
        return await self._db_get(TaskTag, (task_id, tag_id))

    async def create(self, task_id: uuid.UUID, tag_id: uuid.UUID) -> TaskTag:
        item = TaskTag(task_id=task_id, tag_id=tag_id)
        return await self._db_add(item)

    async def delete(self, task_id: uuid.UUID, tag_id: uuid.UUID) -> None:
        item = await self.get(task_id, tag_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_task(self, task_id: uuid.UUID) -> list[TaskTag]:
        return await self._db_list_by(TaskTag, task_id=task_id)

    async def list_by_tag(self, tag_id: uuid.UUID) -> list[TaskTag]:
        return await self._db_list_by(TaskTag, tag_id=tag_id)
