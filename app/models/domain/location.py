from pydantic import BaseModel, Field


class LocationName(BaseModel):
    name_location: str = Field(None, alias='NameLocation')


class LocationModel(BaseModel):
    model: str = Field(None, alias='Model')


class LocationPrice(BaseModel):
    Price: str = Field(None, alias='Price')


class LocationAddress(BaseModel):
    address: str = Field(None, alias='Address')


class LocationInfo(BaseModel):
    info_location: str = Field(None, alias='InfoLocation')


class LocationTimeStar(BaseModel):
    time_star: str = Field(None, alias='TimeStar')


class LocationPointAddress(BaseModel):
    point_address: list = Field(None, alias='PointAddress')


class LocationPointSpace(BaseModel):
    ponit_space: list = Field(None, alias='PointSpace')


class LocationPointCross(BaseModel):
    point_cross: list = Field(None, alias='PointCross')


class LocationGmail(BaseModel):
    gmail_bussiness: str = Field(None, alias='GmailBussiness')


class LocationIdAddress(BaseModel):
    on_id_address: str = Field(None, alias='OnIdAddress')
