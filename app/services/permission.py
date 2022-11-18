from app.models.schemas import permission as _permission_schemas
from app.db.entity import permission as _permission

from app.db.permission import PermissionRepositories


_repo = PermissionRepositories()


class PermissionService():

    def create_permission(permission_in: _permission_schemas.PermissionIn):
        permission = _permission.PermissionEtity(
            **permission_in.dict(by_alias=True)
        )
        _ = _repo.create_permission(permission.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_permission():
        datas = _repo.get_all_perrmission()
        response = []
        for data in datas:
            response.append({
                'value': data.get('Permission'),
                'text': data.get('Permission')
            })

        return response

    def delete_permission(permission_in: _permission_schemas.PermissionIn):
        permission = _permission.PermissionEtity(
            **permission_in.dict(by_alias=True)
        )
        _ = _repo.delete_permission(permission.pk, permission.sk)
        return {'message': 'delete successfully'}
