from app.models.schemas import type as _type_schemas
from app.db.entity import type as _type

from app.db.type import TypeRepositories


_repo = TypeRepositories()


class typeService():

    def create_type(type_in: _type_schemas.TypeIn):
        type = _type.TypeEtity(
            **type_in.dict(by_alias=True)
        )
        _ = _repo.create_type(type.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_type():
        response = _repo.get_all_type()
        return response

    def delete_type(type_in: _type_schemas.TypeIn):
        type = _type.TypeEtity(
            **type_in.dict(by_alias=True)
        )
        _ = _repo.delete_type(type.pk, type.sk)
        return {'message': 'delete successfully'}
