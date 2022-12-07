from app.models.schemas import contact as _contact_schemas
from app.db.entity.base import BaseEntity



class contactEtity(
    BaseEntity,
    _contact_schemas.ContactIn
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'CONTACT#{self.number}'
        self.sk = f'CONTACT#{self.number}'

    def get_pk(number: str):
        pk = f'CONTACT#{number}'
        return pk

    def get_sk(number: str):
        sk = f'CONTACT#{number}'
        return sk

    def get_pk_and_sk(number: str):
        pk = contactEtity.get_pk(number)
        sk = contactEtity.get_sk(number)
        return pk, sk
