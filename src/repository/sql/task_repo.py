import uuid

from src.core.db.models import Task
from ..base import BaseRepository


class TaskRepositoryImpl(BaseRepository[Task]):
    async def get_by_id(self, task_id: uuid.UUID) -> Task | None:
        return await self._db_get(Task, task_id)

    async def create(self, data: dict) -> Task:
        item = Task(**data)
        return await self._db_add(item)

    async def update(self, task_id: uuid.UUID, data: dict) -> Task:
        item = await self._db_get(Task, task_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, task_id: uuid.UUID) -> None:
        item = await self._db_get(Task, task_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_project(self, project_id: uuid.UUID) -> list[Task]:
        return await self._db_list_by(Task, project_id=project_id)

    async def list_by_status(self, status_id: uuid.UUID) -> list[Task]:
        return await self._db_list_by(Task, status_id=status_id)
