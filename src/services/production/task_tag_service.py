from uuid import UUID

from src.repository import Store
from src.schemas.dtos import TaskTagDTO

from ..interfaces import BaseService


class TaskTagServiceImpl(BaseService[TaskTagDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id: tuple[UUID, UUID]) -> TaskTagDTO | None:
        item = await self.store.task_tag_repo().get_by_id(item_id)
        return item

    async def create(self, data: dict) -> TaskTagDTO:
        item = await self.store.task_tag_repo().create(data)
        return item

    async def update(self, item_id: tuple[UUID, UUID], data: dict) -> TaskTagDTO:
        item = await self.store.task_tag_repo().update(item_id, data)
        return item

    async def delete(self, item_id: tuple[UUID, UUID]) -> None:
        await self.store.task_tag_repo().delete(item_id)

    async def get_all(self) -> list[TaskTagDTO]:
        items = await self.store.task_tag_repo().get_all()
        return items

    async def attach_tags(self, task_id: UUID, tag_ids: list[UUID]) -> list[UUID]:
        existing_items = await self.store.task_tag_repo().get_by_task_id(task_id)
        existing_tag_ids = {item.tag_id for item in existing_items}

        for tag_id in tag_ids:
            if tag_id not in existing_tag_ids:
                await self.create({"task_id": task_id, "tag_id": tag_id})

        updated_items = await self.store.task_tag_repo().get_by_task_id(task_id)
        return [item.tag_id for item in updated_items]
