from typing import AsyncIterator

from src.services import Service, ServiceImpl
from src.repository.store import StoreImpl
from src.core.db.uow import UnitOfWork

unit_of_work = UnitOfWork()

async def get_service_manager() -> AsyncIterator[Service]:
    async with unit_of_work() as session:
        store = StoreImpl(session)
        yield ServiceImpl(store)    
