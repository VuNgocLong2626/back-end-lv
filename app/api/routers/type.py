from fastapi import APIRouter
from app.models.schemas import type as _schemas_type
from app.services.type import typeService
from typing import List


router = APIRouter()


@router.post('/create-type')
async def create_type(type_in: _schemas_type.TypeIn):
    response = typeService.create_type(type_in)
    return response


@router.get("/get-all-type", response_model=List[_schemas_type.TypeIn])
async def get_all():
    response = typeService.get_all_type()
    return response


@router.delete('/delete-type')
async def delete_type(per_in: _schemas_type.TypeIn):
    response = typeService.delete_type(per_in)
    return response
