import uuid
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import Comment
from src.schemas.dtos import CommentDTO
from src.core.utils import map_model

from ..interfaces import BaseRepository


class CommentRepositoryImpl(BaseRepository[Comment]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> CommentDTO | None:
        item = await Comment.get_by_id(self.session, item_id)
        if item is None:
            return None
        return map_model(item, CommentDTO)

    async def create(self, data: dict) -> CommentDTO:
        item = Comment.from_dict(data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, CommentDTO)

    async def update(self, item_id: uuid.UUID, data: dict) -> CommentDTO | None:
        item = await Comment.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        saved_item = await item.save(self.session)
        return map_model(saved_item, CommentDTO)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await Comment.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[CommentDTO]:
        items = await Comment.get_all(self.session)
        return [map_model(i, CommentDTO) for i in items]

    async def get_all_by_task(
        self, task_id: uuid.UUID, limit: int, offset: int
    ) -> tuple[list[CommentDTO], int]:
        stmt = (
            select(Comment)
            .where(Comment.task_id == task_id)
            .order_by(Comment.created_at.asc())
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(stmt)
        items = result.scalars().all()
        dto_items = [map_model(i, CommentDTO) for i in items]

        count_stmt = select(func.count()).where(Comment.task_id == task_id)
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return dto_items, total
