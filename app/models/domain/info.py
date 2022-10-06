from pydantic import BaseModel, Field


class InfoFullName(BaseModel):
    fullname: str = Field(alias='FullName')


class InfoNumber(BaseModel):
    number: str = Field(alias='Number')


class InfoCMND(BaseModel):
    cmnd: int = Field(alias='CMND')


class InfoPath(BaseModel):
    path: str = Field(alias='Path')
