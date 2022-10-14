from app.models.domain import permission as _permission_domain
from app.models.domain import base as _base_domain


class PermissionIn(
    _permission_domain.PermissionName
):
    pass


class PermissionDB(
    _permission_domain.PermissionName
):
    pass