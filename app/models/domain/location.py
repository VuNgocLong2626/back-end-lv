from pydantic import BaseModel, Field


class LocationName(BaseModel):
    name: str = Field(None, alias='Name')


class LocationModel(BaseModel):
    model: str = Field(None, alias='Model')


class LocationCost(BaseModel):
    cost: int = Field(None, alias='Cost')


class LocationAddress(BaseModel):
    address: str = Field(None, alias='Address')


class LocationInfo(BaseModel):
    info: str = Field(None, alias='Info')
