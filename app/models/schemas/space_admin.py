from app.models.domain import space as _domain_space
from app.models.domain import base as _domain_base
from app.models.domain import type as _domain_type


class SpaceAdminIn(
    _domain_space.SpaceName,
    _domain_type.TypeName,
    _domain_space.SpacePoint
):
    pass


class SpaceAdminInDB(
    _domain_base.IdSpace,
    _domain_space.SpaceName,
    _domain_type.TypeName,
    _domain_space.SpacePoint
):
    pass


class SpaceAdminDelete(
    _domain_base.IdSpace
):
    pass
