from app.models.schemas import type as _type_schemas
from app.db.entity.base import BaseEntity


class TypeEtity(
    BaseEntity,
    _type_schemas.TypeIn
):
    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'TYPE#{self.type}'
        self.sk = f'TYPE#{self.type}'

    def get_pk(type: str):
        pk = f'TYPE#{type}'
        return pk

    def get_sk(type: str):
        sk = f'TYPE#{type}'
        return sk

    def get_pk_and_sk(type: str):
        pk = TypeEtity.get_pk(type)
        sk = TypeEtity.get_sk(type)
        return pk, sk

