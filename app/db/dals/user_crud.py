from fastapi import HTTPException

from ..db_models import User
from sqlalchemy.ext.asyncio import AsyncSession
from ...schemas.user_schemas import UserCreate

class UserDAL:

    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    def create_user(self, user: UserCreate) -> User:
        try:
            new_user = User(**user.model_dump())
            new_user.set_password(new_user.password)
            self.db_session.add(new_user)
            return new_user
        except Exception as e:
            raise HTTPException(status_code=432, detail=str(e))

