from pydantic import BaseModel, Field


class SpacePoint(BaseModel):
    point: list = Field(None, alias='Point')


class SpaceName(BaseModel):
    space_name: str = Field(None, alias='SpaceName')
