from pydantic import BaseModel, Field


class NeighbourNumber(BaseModel):
    number_neighbour: str = Field(None, alias='NumberNeighbour')


class NeighbourListAddress(BaseModel):
    list_address_neighbour: list = Field([], alias='ListAddressNeighbour')


class NeighbourListLocation(BaseModel):
    list_location: list = Field([], alias='ListLocation')


class NeighbourPath(BaseModel):
    path: str = Field(None, alias='Path')
