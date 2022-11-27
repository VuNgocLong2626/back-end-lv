from app.models.schemas import location as location_schemas
from app.db.entity.base import BaseEntity, GSI2
from ksuid import Ksuid


class LocationEtity(
    BaseEntity,
    location_schemas.LocationInData,
    GSI2
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        if not self.id_location:
            self.id_location = str(Ksuid())
        self.point_address = str(self.point_address)
        self.ponit_space = str(self.ponit_space)
        self.point_cross = str(self.point_cross)
        self.pk = f'LOCATION#{self.id_location}'
        self.sk = f'LOCATION#{self.id_location}'
        self.gsi2pk = f'ACCOUNT#{self.gmail_bussiness}'
        self.gsi2sk = f'LOCATION#{self.id_location}'

    def get_pk(space_admin: str):
        pk = f'SPACE#{space_admin}'
        return pk

    def get_sk(space_admin: str):
        sk = f'SPACE#{space_admin}'
        return sk

    def get_pk_and_sk(space_admin: str):
        pk = LocationEtity.get_pk(space_admin)
        sk = LocationEtity.get_sk(space_admin)
        return pk, sk
