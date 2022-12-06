from app.models.schemas import neighbour as _neighbour_schemas
from app.db.entity.base import BaseEntity

class neighbourEtity(
    BaseEntity,
    _neighbour_schemas.NeighbourInData
):

    def __init__(self, *args, **kwargs):

        super().__init__(**kwargs)
        self.pk = f'NEIGHBOUR#{self.id_space}'
        self.sk = f'NEIGHBOUR#{self.id_space}'

    def get_pk(gmail: str):
        pk = f'NEIGHBOUR#{gmail}'
        return pk

    def get_sk(gmail: str):
        sk = f'NEIGHBOUR#{gmail}'
        return sk

    def get_pk_and_sk(gmail: str):
        pk = neighbourEtity.get_pk(gmail)
        sk = neighbourEtity.get_sk(gmail)
        return pk, sk
