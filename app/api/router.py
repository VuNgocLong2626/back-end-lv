
from fastapi import APIRouter

from app.api.routers import (
    test as api_basic,
    account as api_account,
    permission as api_permission
)


router = APIRouter()


router.include_router(
    api_basic.router,
    prefix="/basic",
    tags=["Basic"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_account.router,
    prefix="/account",
    tags=["Accout"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_permission.router,
    prefix="/permission",
    tags=["Permission"],
    responses={404: {"description": "Not found"}}
)
