from app.models.schemas import space_admin as _space_admin_schemas
from app.db.entity.base import BaseEntity, GSI2
from ksuid import Ksuid


class SpaceAdminEtity(
    BaseEntity,
    _space_admin_schemas.SpaceAdminInDB,
    GSI2
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        if not self.id_space:
            self.id_space = str(Ksuid())
        self.point = str(self.point)
        self.pk = f'SPACE#{self.id_space}'
        self.sk = f'SPACE#{self.id_space}'
        self.gsi2pk = f'TYPE#{self.type}'
        self.gsi2sk = f'SPACE#{self.id_space}'

    def get_pk(space_admin: str):
        pk = f'SPACE#{space_admin}'
        return pk

    def get_sk(space_admin: str):
        sk = f'SPACE#{space_admin}'
        return sk

    def get_pk_and_sk(space_admin: str):
        pk = SpaceAdminEtity.get_pk(space_admin)
        sk = SpaceAdminEtity.get_sk(space_admin)
        return pk, sk
