from app.models.schemas import info as _info_schemas
from app.db.entity.base import BaseEntity
from app.utils import auth as _auth
from ksuid import Ksuid
from app.utils.aws import s3 as _s3


class InfoEtity(
    BaseEntity,
    _info_schemas.InfoData
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        if self.path:
            file_name = _s3.get_file_name(self.path, str(Ksuid()))
            self.path = file_name
        self.pk = f'INFO#{self.gmail}'
        self.sk = f'INFO#{self.gmail}'

    def get_pk(gmail: str):
        pk = f'INFO#{gmail}'
        return pk

    def get_sk(gmail: str):
        sk = f'INFO#{gmail}'
        return sk

    def get_pk_and_sk(gmail: str):
        pk = InfoEtity.get_pk(gmail)
        sk = InfoEtity.get_sk(gmail)
        return pk, sk
