from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class AuthRegisterRequest(BaseModel):
    email: EmailStr
    password: str
    name: str


class AuthLoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthRegisterResponseUser(BaseModel):
    id: UUID
    email: EmailStr
    name: str
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime


class AuthRegisterResponse(BaseModel):
    user: AuthRegisterResponseUser


class AuthLoginResponse(BaseModel):
    access_token: str
    expires_in: int
