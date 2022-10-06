from pydantic import BaseModel, Field


class TypeName(BaseModel):
    name: str = Field(None, alias='Name')
