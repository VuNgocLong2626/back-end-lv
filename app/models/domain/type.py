from pydantic import BaseModel, Field


class TypeName(BaseModel):
    type: str = Field(None, alias='Type')
