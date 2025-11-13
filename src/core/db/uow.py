from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.db import async_session_maker


class UnitOfWork:
    def __init__(self):
        self.session: AsyncSession | None = None

    @asynccontextmanager
    async def __call__(self) -> AsyncIterator[AsyncSession]:
        async with async_session_maker() as session:
            self.session = session
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()
