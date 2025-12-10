from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr

from .common import Paginated


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime


class UserUpdateRequest(BaseModel):
    name: str | None = None
    avatar_url: str | None = None


class UserListResponse(Paginated[UserResponse]): ...
