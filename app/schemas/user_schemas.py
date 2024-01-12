import uuid
from pydantic import BaseModel, EmailStr, field_validator


class TunedModel(BaseModel):

    class Config:

        from_attributes = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserShow(TunedModel):

    username: str
    email: EmailStr


