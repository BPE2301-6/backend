from uuid import UUID

from src.repository import Store
from src.schemas.dtos import TaskDTO

from ..interfaces import BaseService


class TaskServiceImpl(BaseService[TaskDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: UUID) -> TaskDTO | None:
        item = await self.store.task_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> TaskDTO:
        data.pop("tag_ids", None)
        # TODO: обновление таблицы task_tag

        project_id: UUID = data["project_id"]
        project_key = await self.store.project_repo().get_key_by_id(project_id)
        seq = await self.store.task_sequence_repo().reserve_next_seq(project_id)

        data["seq"] = seq
        data["key"] = f"{project_key}-{seq}"

        item = await self.store.task_repo().create(data)
        return item

    async def update(self, item_id: UUID, data: dict) -> TaskDTO:
        item = await self.store.task_repo().update(item_id, data)
        return item

    async def delete(self, item_id: UUID) -> None:
        await self.store.task_repo().delete(item_id)

    async def get_all(self) -> list[TaskDTO]:
        items = await self.store.task_repo().get_all()
        return items

    async def get_all_by_project(
        self, project_id: UUID, filters: dict, limit: int, offset: int, sort: str
    ) -> tuple[list[TaskDTO], int]:
        items, total = await self.store.task_repo().get_all_by_project(
            project_id, filters, limit, offset, sort
        )
        return items, total
