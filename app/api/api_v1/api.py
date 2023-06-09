from fastapi import APIRouter

from app.api.api_v1.endpoints import login, fastapi

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(fastapi.router, prefix="/fastapi", tags=["fastapi"])
