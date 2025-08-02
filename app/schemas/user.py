from enum import Enum

from pydantic import BaseModel, Field, field_validator


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


class CreateUserRequest(BaseModel):
    user_name: str = Field(
        ...,
        min_length=5,
        description="user1234"
    )
    password: str = Field(
        ...,
        min_length=8,
        description="Password should be at least 8 chars"
    )
    user_role: UserRole = Field(default="user")

    @field_validator("user_name", "password")
    def no_spaces_allowed(cls, v: str):
        if " " in v:
            raise ValueError("Spaces are not allowed.")
        return v


class UserRead(BaseModel):
    id: int
    user_name: str
    user_role: str
