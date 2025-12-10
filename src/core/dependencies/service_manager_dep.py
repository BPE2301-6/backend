from collections.abc import AsyncIterator

from src.core.db.uow import UnitOfWork
from src.repository.store import StoreImpl
from src.services import Service, ServiceImpl

unit_of_work = UnitOfWork()


async def get_service_manager() -> AsyncIterator[Service]:
    async with unit_of_work() as session:
        store = StoreImpl(session)
        yield ServiceImpl(store)
