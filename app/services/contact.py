from app.models.schemas import contact as _contact_schemas
from app.db.entity import contact as _contact

from app.db.contact import contactRepositories


_repo = contactRepositories()


class contactService():

    def create_contact(contact_in: _contact_schemas.ContactIn):
        contact = _contact.contactEtity(
            **contact_in.dict(by_alias=True)
        )
        _ = _repo.create_contact(contact.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_contact():
        response = _repo.get_all_contact()
        return response

    def delete_contact(contact_in: str):
        pk, sk = _contact.contactEtity.get_pk_and_sk(contact_in)
        _ = _repo.delete_contact(pk, sk)
        return {'message': 'delete successfully'}
