from app.models.domain import location as _domain_location
from app.models.domain import base as _domain_base
from pydantic import BaseModel, Field



class LocationIn(
    _domain_location.LocationGmail,
    _domain_location.LocationName,
    _domain_location.LocationPrice,
    _domain_location.LocationAddress,
    _domain_location.LocationInfo,
    _domain_location.LocationTimeStar,
    _domain_location.LocationPointAddress,
    _domain_location.LocationPointSpace,
    _domain_location.LocationPointCross,
    _domain_location.LocationModel

):
    pass


class LocationInData(
    _domain_base.IdLocation,
    _domain_location.LocationGmail,
    _domain_location.LocationName,
    _domain_location.LocationPrice,
    _domain_location.LocationAddress,
    _domain_location.LocationInfo,
    _domain_location.LocationTimeStar,
    _domain_location.LocationPointAddress,
    _domain_location.LocationPointSpace,
    _domain_location.LocationPointCross,
    _domain_location.LocationModel,
    _domain_location.LocationIdAddress

):
    pass


class LocationDelete(
    _domain_base.IdLocation
):
    pass


class LocationGetInfo(
    _domain_location.LocationGmail
):
    pass


class LocationUpdate(
    _domain_location.LocationName,
    _domain_location.LocationPrice,
    _domain_location.LocationAddress,
    _domain_location.LocationInfo,
    _domain_location.LocationTimeStar,
    _domain_location.LocationModel,
    _domain_base.PartitionKey,
    _domain_base.SortKey
):
    pass


class LocationListId(BaseModel):
    list_id_location: list = Field(None, alias='ListIdLocation')


class LocationUpdateIdAddress(
    _domain_location.LocationIdAddress
):
    pass