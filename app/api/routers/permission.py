from fastapi import APIRouter
from app.models.schemas import permission as _schemas_permission
from app.services.permission import PermissionService
from typing import List


router = APIRouter()


@router.post('/create-permission')
async def create_permission(permission_in: _schemas_permission.PermissionIn):
    response = PermissionService.create_permission(permission_in)
    return response


@router.get("/get-all-permission", response_model=List[_schemas_permission.PermissionDB])
async def get_all():
    response = PermissionService.get_all_permission()
    return response


@router.delete('/delete-permission')
async def delete_permission(per_in: _schemas_permission.PermissionIn):
    response = PermissionService.delete_permission(per_in)
    return response
