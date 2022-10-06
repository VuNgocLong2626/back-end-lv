from pydantic import BaseModel, Field


class SpacePoint(BaseModel):
    point: list = Field(None, alias='Point')
