from pydantic import BaseModel, Field


class PermissionName(BaseModel):
    name: str = Field(None, alias='Name')
