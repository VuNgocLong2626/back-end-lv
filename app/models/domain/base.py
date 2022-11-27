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


class IdComment(BaseModel):
    id_comment: str = Field(None, alias='IdComment')


class GlobalSecondaryIndexesPartitionKey2(BaseModel):
    gsi2pk: str = Field(None, alias="GSI2PK")


class GlobalSecondaryIndexesSortKey2(BaseModel):
    gsi2sk: str = Field(None, alias="GSI2SK")


class GlobalSecondaryIndexesPartitionKey3(BaseModel):
    gsi3pk: str = Field(None, alias="GSI3PK")


class GlobalSecondaryIndexesSortKey3(BaseModel):
    gsi3sk: str = Field(None, alias="GSI3SK")
