from typing import Any

from fastapi import HTTPException, status

from src.core.utils import AuthUtils
from src.repository import Store
from src.schemas.dtos import UserDTO, AuthDTO

from ..interfaces import BaseService


class AuthServiceImpl(BaseService[UserDTO]):
    def __init__(self, store: Store):
        self.store = store

    async def get(self, item_id):
        raise NotImplementedError()

    async def create(self, data):
        raise NotImplementedError()

    async def update(self, item_id, data):
        raise NotImplementedError()

    async def delete(self, item_id):
        raise NotImplementedError()

    async def get_all(self):
        raise NotImplementedError()

    async def register(self, data: dict) -> UserDTO:
        email = data["email"].lower()

        existing = await self.store.user_repo().get_by_email(email)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
            )

        repo_data = {
            "email": email,
            "name": data["name"],
            "hashed_password": AuthUtils.hash(data["password"]),
            "avatar_url": data.get("avatar_url"),
        }

        try:
            user = await self.store.user_repo().create(repo_data)
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create user"
            ) from err

        return user

    async def login(self, data: dict) -> AuthDTO:
        email = data["email"].lower()
        password = data["password"]

        user = await self.store.user_repo().get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )

        if not AuthUtils.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
            )

        token = AuthUtils.create_access_token({"sub": str(user.id)})

        return {"access_token": token, "expires_in": AuthUtils.EXPIRES_IN}
