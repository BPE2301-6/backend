from dataclasses import dataclass


@dataclass
class AuthDTO:
    access_token: str
    expires_in: int
