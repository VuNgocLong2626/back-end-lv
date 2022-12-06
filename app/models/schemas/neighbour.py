from app.models.domain import neighbours as _domain_neighbours
from app.models.domain import base as _domain_base
from pydantic import BaseModel, Field


class NeighbourInData(
    _domain_neighbours.NeighbourNumber,
    _domain_neighbours.NeighbourListAddress,
    _domain_neighbours.NeighbourListLocation,
    _domain_base.IdSpace
):
    pass


class NeighbourIn(
    _domain_base.IdSpace
):
    pass


class NeighbourUpdateListAddress(BaseModel):
    id_space_current: str = Field(None, alias='IdSpaceCurrent')
    id_space_neighbour: str = Field(None, alias='IdSpaceNeighbour')


class NeighbourUpdateListLocation(BaseModel):
    id_location: str = Field(None, alias='IdLocation')
    id_address: str = Field(None, alias='IdAddress')


class NeighbourSearch(BaseModel):
    id_star: str = Field(None, alias='IdStar')
    id_end: str = Field(None, alias='IdEnd')
    address: bool = Field(True, alias='Address')
