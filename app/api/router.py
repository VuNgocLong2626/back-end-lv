
from fastapi import APIRouter

from app.api.routers import (
    test as api_basic,
)


router = APIRouter()


router.include_router(
    api_basic.router,
    prefix="/basic",
    tags=["Basic"],
    responses={404: {"description": "Not found"}}
)
