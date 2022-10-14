from app.models.domain import base as _base_domain


class BaseEntity(
    _base_domain.PartitionKey,
    _base_domain.SortKey
):
    pass


class BaseGlobalSecondaryIndexesEntity(
    _base_domain.GlobalSecondaryIndexesPartitionKey,
    _base_domain.GlobalSecondaryIndexesSortKey
):
    pass
