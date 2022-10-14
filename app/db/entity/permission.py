from app.models.schemas import permission as _permission_schemas
from app.db.entity.base import BaseEntity


class PermissionEtity(
    BaseEntity,
    _permission_schemas.PermissionDB
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'PERMISSION#{self.permission}'
        self.sk = f'PERMISSION#{self.permission}'

    def get_pk(permission: str):
        pk = f'PERMISSION#{permission}'
        return pk

    def get_sk(permission: str):
        sk = f'PERMISSION#{permission}'
        return sk

    def get_pk_and_sk(permission: str):
        pk = PermissionEtity.get_pk(permission)
        sk = PermissionEtity.get_sk(permission)
        return pk, sk
