from src.repository import Store
from ..interfaces import BaseService


class AuthServiceImpl(BaseService):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id): raise NotImplementedError()
    async def create(self, data): raise NotImplementedError()
    async def update(self, item_id, data): raise NotImplementedError()
    async def delete(self, item_id): raise NotImplementedError()
    async def get_all(self): raise NotImplementedError()

    async def register(self, data: dict) -> dict:
        user = await self.store.user_repo().create(data)
        return user

    async def login(self, email: str, password: str) -> dict:
        user = await self.store.user_repo().get_by_email(email)

        return {
            "access_token": "jwt-token-stub",
            "expires_in": 3600,
        }
