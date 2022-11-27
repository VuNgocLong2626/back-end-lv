from fastapi import APIRouter, UploadFile, File, Form
from app.models.schemas import location as _schemas_location
from app.services.location import LocationService
from typing import List


router = APIRouter()


@router.post('/create-location', response_model=_schemas_location.LocationDelete)
async def create_location(location_in: _schemas_location.LocationIn):
    response = LocationService.create_location(location_in)
    return response


@router.get("/get-all-location")
async def get_all():
    response = LocationService.get_all_location()
    return response


@router.get("/get-all-location-image")
async def get_all_image():
    response = LocationService.get_all_location_image()
    return response


@router.get("/get-all-location-point")
async def get_all_point():
    response = LocationService.get_all_location_point()
    return response


@router.get("/get-main-info-location")
async def get_main_info_location():
    response = LocationService.get_main_info_location()
    return response


@router.get("/get-main-info-location-all")
async def get_main_info_location_all():
    response = LocationService.get_main_info_location_all()
    return response


@router.post("/get-info-location-by-gmail")
async def get_info_location(gmail: _schemas_location.LocationGetInfo):
    response = LocationService.get_info_location_by_id(gmail.gmail_bussiness)
    return response


@router.post("/get-info-location-by-id")
async def get_info_location_id(gmail: _schemas_location.LocationDelete):
    response = LocationService.get_info_by_id(gmail)
    return response


@router.delete('/delete-location')
async def delete_location(per_in: _schemas_location.LocationDelete):
    response = LocationService.delete_location(per_in)
    return response


@router.post('/upload-image')
async def upload_image(
    path: List[UploadFile] = File(..., alias='Path'),
    id_location: str = Form(..., alias='IdLocation'),
):
    response = LocationService.upload_image(id_location, path)
    return response


@router.put('/update-info-location')
async def update_info(data: _schemas_location.LocationUpdate):
    response = LocationService.update_info_location(data)
    return response


@router.post("/get-info-list-id")
async def get_info_list_id(gmail: list):
    response = LocationService.get_info_list_id(gmail)
    return response
