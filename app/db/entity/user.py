from app.models.schemas import account as _account_schemas
from app.db.entity.base import BaseEntity


class UserEtity(
    BaseEntity,
    _account_schemas.TokenData
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'ACCOUNT#{self.gmail}'
        self.sk = f'ACCOUNT#{self.gmail}'

    def get_pk(gmail: str):
        pk = f'ACCOUNT#{gmail}'
        return pk

    def get_sk(gmail: str):
        sk = f'ACCOUNT#{gmail}'
        return sk

    def get_pk_and_sk(gmail: str):
        pk = UserEtity.get_pk(gmail)
        sk = UserEtity.get_sk(gmail)
        return pk, sk
