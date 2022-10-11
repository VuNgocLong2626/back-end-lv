from pydantic import BaseModel, Field


class PermissionName(BaseModel):
    permission: str = Field(None, alias='Permission')
