from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class AuthRegisterRequest(BaseModel):
    email: str
    password: str
    name: str


class AuthLoginRequest(BaseModel):
    email: str
    password: str


class AuthRegisterResponseUser(BaseModel):
    id: UUID
    email: str
    name: str
    avatar_url: str | None = None
    created_at: datetime
    updated_at: datetime


class AuthRegisterResponse(BaseModel):
    user: AuthRegisterResponseUser


class AuthLoginResponse(BaseModel):
    access_token: str
    expires_in: int
