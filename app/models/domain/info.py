from pydantic import BaseModel, Field


class InfoFullName(BaseModel):
    fullname: str = Field(None, alias='FullName')


class InfoNumber(BaseModel):
    number: str = Field(None, alias='Number')


class InfoCMND(BaseModel):
    cmnd: int = Field(None, alias='CMND')


class InfoPath(BaseModel):
    path: str = Field(None, alias='Path')
