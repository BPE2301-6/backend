import os
from datetime import UTC, datetime, timedelta

import jwt
from passlib.hash import argon2


class AuthUtils:
    SECRET = os.getenv("JWT_SECRET", "supersecretkey")
    ALGORITHM = "HS256"
    EXPIRES_IN = 3600

    @staticmethod
    def hash(password: str) -> str:
        return argon2.hash(password)

    @staticmethod
    def verify(password: str, hashed: str) -> bool:
        return argon2.verify(password, hashed)

    @classmethod
    def create_access_token(cls, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(seconds=cls.EXPIRES_IN)
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, cls.SECRET, algorithm=cls.ALGORITHM)
        return token

    @classmethod
    def decode_access_token(cls, token: str) -> dict | None:
        try:
            payload = jwt.decode(token, cls.SECRET, algorithms=[cls.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
