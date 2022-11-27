from fastapi import APIRouter
from app.models.schemas import space_admin as _schemas_space_admin
from app.services.space_admin import space_adminService
from typing import List


router = APIRouter()


@router.post('/create-space_admin')
async def create_space_admin(space_admin_in: _schemas_space_admin.SpaceAdminIn):
    response = space_adminService.create_space_admin(space_admin_in)
    return response


@router.get("/get-all-space_admin")
async def get_all():
    response = space_adminService.get_all_space_admin()
    return response


@router.get("/get-all-space")
async def get_all():
    response = space_adminService.get_all_space_()
    return response


@router.delete('/delete-space_admin')
async def delete_space_admin(per_in: _schemas_space_admin.SpaceAdminDelete):
    response = space_adminService.delete_space_admin(per_in)
    return response


@router.get("/get-all-space-selection")
async def get_all():
    response = space_adminService.get_all_space_selection()
    return response
