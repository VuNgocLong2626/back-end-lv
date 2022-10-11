from app.models.schemas import permission as _permission_schemas
from app.db.entity.base import BaseEntity


class PermissionEtity(
    BaseEntity,
    _permission_schemas.PermissionDB
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'PERMISSION#{self.name}'
        self.sk = f'PERMISSION#{self.name}'

    def get_pk(name: str):
        pk = f'PERMISSION#{name}'
        return pk

    def get_sk(name: str):
        sk = f'PERMISSION#{name}'
        return sk

    def get_pk_and_sk(name: str):
        pk = PermissionEtity.get_pk(name)
        sk = PermissionEtity.get_sk(name)
        return pk, sk
