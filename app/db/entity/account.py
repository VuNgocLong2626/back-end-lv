from app.models.schemas import account as _account_schemas
from app.db.entity.base import BaseEntity, BaseGlobalSecondaryIndexesEntity
from app.utils import auth as _auth
from ksuid import Ksuid
from app.utils.aws import s3 as _s3


class AccountEtity(
    BaseEntity,
    _account_schemas.AccountDB,
    BaseGlobalSecondaryIndexesEntity
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        hash_passwoed = _auth.get_password_hash(self.password)
        self.password = hash_passwoed
        self.pk = f'ACCOUNT#{self.gmail}'
        self.sk = f'ACCOUNT#{self.gmail}'
        self.gsi1pk = f'ACCOUNT#{self.gmail}'
        self.gsi1sk = f'PERMISSION#{self.permission}'

    def get_pk(gmail: str):
        pk = f'ACCOUNT#{gmail}'
        return pk

    def get_sk(gmail: str):
        sk = f'ACCOUNT#{gmail}'
        return sk

    def get_gsi1pk(gmail: str):
        pk = f'ACCOUNT#{gmail}'
        return pk

    def get_gsi1sk(permission: str):
        gsi1sk = f'PERMISSION#{permission}'
        return gsi1sk

    def get_pk_and_sk(gmail: str):
        pk = AccountEtity.get_pk(gmail)
        sk = AccountEtity.get_sk(gmail)
        return pk, sk

    def get_gsi1(gmail: str, permission: str):
        gsi1pk = AccountEtity.get_gsi1pk
        gsi1sk = AccountEtity.get_gsi1sk
        return gsi1pk, gsi1sk
