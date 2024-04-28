from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from src.entity.models import Role


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=5, max_length=10)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    email: EmailStr
    avatar: str
    role: Role

    model_config = ConfigDict(from_attributes = True)


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr


class ResetPassword(BaseModel):
    password1: str
    password2: str
