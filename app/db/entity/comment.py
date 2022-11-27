from app.models.schemas import comment as _comment_schemas
from app.db.entity.base import BaseEntity, BaseGlobalSecondaryIndexesEntity
from ksuid import Ksuid


class CommentEtity(
    BaseEntity,
    _comment_schemas.CommentInData,
    BaseGlobalSecondaryIndexesEntity
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        if not self.id_comment:
            self.id_comment = str(Ksuid())
        self.pk = f'COMMENT#{self.id_comment}'
        self.sk = f'COMMENT#{self.id_comment}'
        self.gsi1pk = f'LOCATION#{self.id_location}'
        self.gsi1sk = f'COMMENT#{self.id_comment}'

    def get_pk(comment_admin: str):
        pk = f'COMMENT#{comment_admin}'
        return pk

    def get_sk(comment_admin: str):
        sk = f'COMMENT#{comment_admin}'
        return sk

    def get_pk_and_sk(COMMENT_admin: str):
        pk = CommentEtity.get_pk(COMMENT_admin)
        sk = CommentEtity.get_sk(COMMENT_admin)
        return pk, sk
