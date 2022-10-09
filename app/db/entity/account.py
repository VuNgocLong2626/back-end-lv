from app.models.schemas import account as _account_schemas
from app.db.entity.base import BaseEntity
from app.utils import auth as _auth


class AccountEtity(
    BaseEntity,
    _account_schemas.AccountRegister
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        hash_passwoed = _auth.get_password_hash(self.password)
        self.password = hash_passwoed
        self.pk = f'ACCOUNT#{self.gmail}'
        self.sk = f'ACCOUNT#{self.gmail}'

    def get_pk(gmail: str):
        pk = f'ACCOUNT#{gmail}'
        return pk

    def get_sk(gmail: str):
        sk = f'ACCOUNT#{gmail}'
        return sk

    def get_pk_and_sk(gmail: str):
        pk = AccountEtity.get_pk(gmail)
        sk = AccountEtity.get_sk(gmail)
        return pk, sk
