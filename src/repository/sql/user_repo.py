import uuid

from sqlalchemy import func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.models import User

from ..interfaces import BaseRepository


class UserRepositoryImpl(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, item_id: uuid.UUID) -> User | None:
        return await User.get_by_id(self.session, item_id)

    async def create(self, data: dict) -> User:
        item = User.from_dict(data)
        return await item.save(self.session)

    async def update(self, item_id: uuid.UUID, data: dict) -> User | None:
        item = await User.get_by_id(self.session, item_id)
        if item is None:
            return None
        item.update(**data)
        return await item.save(self.session)

    async def delete(self, item_id: uuid.UUID) -> None:
        item = await User.get_by_id(self.session, item_id)
        if item is not None:
            await item.delete(self.session)

    async def get_all(self) -> list[User]:
        return await User.get_all(self.session)

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def get_list(self, search: str | None, limit: int, offset: int) -> tuple[list[User], int]:
        stmt = select(User)

        if search:
            query = f"%{search}%"
            stmt = stmt.where(or_(User.name.ilike(query), User.email.ilike(query)))

        stmt = stmt.offset(offset).limit(limit)
        result = await self.session.execute(stmt)
        items = result.scalars().all()

        count_stmt = select(func.count()).select_from(User)
        if search:
            count_stmt = count_stmt.where(or_(User.name.ilike(query), User.email.ilike(query)))
        total_result = await self.session.execute(count_stmt)
        total = total_result.scalar_one()

        return items, total
