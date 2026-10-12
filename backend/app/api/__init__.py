from fastapi import APIRouter
from app.api.auth import router as auth_router

api = APIRouter(prefix="/api")
api.include_router(auth_router)