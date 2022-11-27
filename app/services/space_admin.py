from app.models.schemas import space_admin as _space_admin_schemas
from app.db.entity import space_admin as _space_admin

from app.db.space_admin import SpaceRepositories
from functools import partial
import ast

_repo = SpaceRepositories()


class space_adminService():

    def create_space_admin(space_admin_in: _space_admin_schemas.SpaceAdminIn):
        space_admin = _space_admin.SpaceAdminEtity(
            **space_admin_in.dict(by_alias=True)
        )
        _ = _repo.create_space(space_admin.dict(by_alias=True))
        return {'message': 'create successfully'}

    def get_all_space_admin():
        space_all = _repo.get_all_space()
        li = []
        for item in space_all:
            li.append(ast.literal_eval(item.get('Point')))
        # response = list(
        #     map(lambda x: ast.literal_eval(x.get('Point')), space_all))
        # for item in response:
        #     li.extend(item)
        return li

    def get_all_space_():
        space_all = _repo.get_all_space()
        response = []
        for item in space_all:
            # response.append(ast.literal_eval(item.get('Point')))
            response.append({
                'Point':  ast.literal_eval(item.get('Point')),
                'SpaceName': item.get('SpaceName'),
                'IdSpace': item.get('IdSpace')
            })

        return response

    def delete_space_admin(space_admin_in: _space_admin_schemas.SpaceAdminDelete):
        space_admin = _space_admin.SpaceAdminEtity(
            **space_admin_in.dict(by_alias=True)
        )
        _ = _repo.delete_space(space_admin.pk, space_admin.sk)
        return {'message': 'delete successfully'}

    def get_all_space_selection():
        space_all = _repo.get_all_space()
        response = []
        for item in space_all:
            response.append({
                'value':  ast.literal_eval(item.get('Point')),
                'text': item.get('SpaceName'),
                'IdSpace': item.get('IdSpace')
            })

        return response
    