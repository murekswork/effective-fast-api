from fastapi import FastAPI, APIRouter
from app.routers.item_handlers import item_router
from app.routers.user_handlers import user_router
from app.routers.app_handlers import app_router

app = FastAPI(title='Marketplace')

main_router = APIRouter()
main_router.include_router(user_router, prefix='/user', tags=['user'])
main_router.include_router(item_router, prefix='/item', tags=['item'])
main_router.include_router(app_router, prefix='/app')
app.include_router(main_router)
