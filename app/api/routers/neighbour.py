from fastapi import APIRouter
from app.models.schemas import neighbour as _schemas_neighbour
from app.services.neighbour import neighbourService
from typing import List


router = APIRouter()


@router.post('/create-neighbour')
async def create_neighbour(neighbour_in: _schemas_neighbour.NeighbourIn):
    response = neighbourService.create_neighbour(neighbour_in)
    return response


@router.get("/get-all-neighbour")
async def get_all():
    response = neighbourService.get_all_neighbour()
    return response


@router.delete('/delete-neighbour')
async def delete_neighbour(per_in: _schemas_neighbour.NeighbourIn):
    response = neighbourService.delete_neighbour(per_in)
    return response


@router.put('/update-list-address')
async def update_list_address(per_in: _schemas_neighbour.NeighbourUpdateListAddress):
    response = neighbourService.update_list_address(per_in)
    return response


@router.post("/search-addresss")
async def get_all(data_in: _schemas_neighbour.NeighbourSearch):
    response = neighbourService.search_address(data_in)
    return response
