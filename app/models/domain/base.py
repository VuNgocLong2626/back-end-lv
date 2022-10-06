from pydantic import BaseModel, Field


class PartitionKey(BaseModel):
    pk: str = Field(None, alias="PK")


class SortKey(BaseModel):
    sk: str = Field(None, alias="SK")


class GlobalSecondaryIndexesPartitionKey(BaseModel):
    gsi1pk: str = Field(None, alias="GSI1PK")


class GlobalSecondaryIndexesSortKey(BaseModel):
    gsi1sk: str = Field(None, alias="GSI1SK")


class IdLocation(BaseModel):
    id_location: str = Field(None, alias='IdLocation')


class IdSpace(BaseModel):
    id_space: str = Field(None, alias='IdSpace')
