import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import ChecklistItem
from src.schemas.dtos import ChecklistItemDTO
from src.core.utils import map_model  

from ..interfaces import BaseRepository


class ChecklistItemRepositoryImpl(BaseRepository[ChecklistItem]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> ChecklistItemDTO | None:
        item = await ChecklistItem.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, ChecklistItemDTO)

    async def create(self, data: dict) -> ChecklistItemDTO:
        item = ChecklistItem.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ChecklistItemDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> ChecklistItemDTO | None:
        item = await ChecklistItem.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, ChecklistItemDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await ChecklistItem.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[ChecklistItemDTO]:
        items = await ChecklistItem.get_all(self.session)
        return [map_model(i, ChecklistItemDTO) for i in items]
