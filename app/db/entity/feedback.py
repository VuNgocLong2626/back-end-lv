from app.models.schemas import feedback as _feedback_schemas
from app.db.entity.base import BaseEntity


class FeedbackEtity(
    BaseEntity,
    _feedback_schemas.FeedBackOut
):
    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'FEEDBACK#{self.number}'
        self.sk = f'FEEDBACK#{self.number}'

    def get_pk(number: str):
        pk = f'FEEDBACK#{number}'
        return pk

    def get_sk(number: str):
        sk = f'FEEDBACK#{number}'
        return sk

    def get_pk_and_sk(number: str):
        pk = FeedbackEtity.get_pk(number)
        sk = FeedbackEtity.get_sk(number)
        return pk, sk
