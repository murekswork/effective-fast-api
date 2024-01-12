from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.user_schemas import UserCreate, UserShow
from ..db.session import get_db
from ..db.dals.user_crud import UserDAL

user_router = APIRouter()


@user_router.post("/create", response_model=UserShow)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await _create_user(user, db)
    return new_user

async def _create_user(user: UserCreate, db: AsyncSession) -> UserShow:
    async with db as db_session:
        async with db_session.begin():
            user_DAL = UserDAL(db_session=db_session)
            new_user = user_DAL.create_user(user)
            return UserShow(**new_user.__dict__)



