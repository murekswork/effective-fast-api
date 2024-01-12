from fastapi import APIRouter
from fastapi.responses import JSONResponse
app_router = APIRouter()


@app_router.get('')
async def home() -> JSONResponse:
    return JSONResponse({'message': 'Hello World!'})

