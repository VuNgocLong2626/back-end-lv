
from fastapi import APIRouter

from app.api.routers import (
    test as api_basic,
    account as api_account,
    permission as api_permission,
    feedback as api_feedback,
    type as api_type,
    space_admin as api_space_admin,
    location as api_location,
    comment as api_comment,
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

router.include_router(
    api_feedback.router,
    prefix="/feedback",
    tags=["Feedback"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_type.router,
    prefix="/type",
    tags=["type"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_space_admin.router,
    prefix="/space-admin",
    tags=["SpaceAdmin"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_location.router,
    prefix="/location",
    tags=["Location"],
    responses={404: {"description": "Not found"}}
)


router.include_router(
    api_comment.router,
    prefix="/comment",
    tags=["Comment"],
    responses={404: {"description": "Not found"}}
)
