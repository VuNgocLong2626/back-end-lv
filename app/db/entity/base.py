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


class GSI2(
    _base_domain.GlobalSecondaryIndexesPartitionKey2,
    _base_domain.GlobalSecondaryIndexesSortKey2
):
    pass


class GSI3(
    _base_domain.GlobalSecondaryIndexesPartitionKey3,
    _base_domain.GlobalSecondaryIndexesSortKey3
):
    pass
