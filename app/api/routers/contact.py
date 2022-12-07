from fastapi import APIRouter
from app.models.schemas import contact as _schemas_contact
from app.services.contact import contactService
from typing import List


router = APIRouter()


@router.post('/create-contact')
async def create_contact(contact_in: _schemas_contact.ContactIn):
    response = contactService.create_contact(contact_in)
    return response


@router.get("/get-all-contact")
async def get_all():
    response = contactService.get_all_contact()
    return response


@router.delete('/delete-contact')
async def delete_contact(number: str):
    response = contactService.delete_contact(number)
    return response
