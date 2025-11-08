import uuid

from src.core.db.models import ChecklistItem
from ..base import BaseRepository


class ChecklistItemRepositoryImpl(BaseRepository[ChecklistItem]):
    async def get_by_id(self, checklist_item_id: uuid.UUID) -> ChecklistItem | None:
        return await self._db_get(ChecklistItem, checklist_item_id)

    async def create(self, data: dict) -> ChecklistItem:
        item = ChecklistItem(**data)
        return await self._db_add(item)

    async def update(self, checklist_item_id: uuid.UUID, data: dict) -> ChecklistItem | None:
        item = await self._db_get(ChecklistItem, checklist_item_id)
        if item is None:
            return None
        return await self._db_update(item, data)

    async def delete(self, checklist_item_id: uuid.UUID) -> None:
        item = await self._db_get(ChecklistItem, checklist_item_id)
        if item is not None:
            await self._db_delete(item)

    async def list_by_checklist(self, checklist_id: uuid.UUID) -> list[ChecklistItem]:
        return await self._db_list_by(ChecklistItem, checklist_id=checklist_id)
