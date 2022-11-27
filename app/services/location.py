from fastapi import UploadFile
from app.models.schemas import location as _location_schemas
from app.db.entity import location as _location
from app.utils.aws import s3 as _s3
from ksuid import Ksuid
from typing import List
import ast

from app.db.location import LocationRepositories


_repo = LocationRepositories()


class LocationService():

    def create_location(location_in: _location_schemas.LocationIn):
        location = _location.LocationEtity(
            **location_in.dict(by_alias=True)
        )
        _ = _repo.create_location(location.dict(by_alias=True))
        return location

    def get_all_location():
        datas = _repo.get_all_location()
        return datas

    def delete_location(location_in: _location_schemas.LocationDelete):
        location = _location.LocationEtity(
            **location_in.dict(by_alias=True)
        )
        all_image = _repo.get_image_locatio_by_id(
            f'IMAGE#{location.id_location}', f'IMAGE#{location.id_location}').get('ListImage')
        for item in all_image:
            _ = _s3.delete_file(item)
        _ = _repo.delete_location(location.pk, location.sk)
        _ = _repo.delete_location(
            f'IMAGE#{location.id_location}', f'IMAGE#{location.id_location}')
        return {'message': 'delete successfully'}

    def upload_image(
        id_location: str,
        path: List[UploadFile]
    ):
        list_path = []
        for item in path:
            file_name = f'bussiness/{_s3.get_file_name(item.filename, str(Ksuid()))}'
            _ = _s3.upload_file(item, file_name)
            list_path.append(file_name)
        _ = _repo.create_location({
            'PK': f'IMAGE#{id_location}',
            'SK': f'IMAGE#{id_location}',
            'IdLocation': id_location,
            'ListImage': list_path
        })
        return list_path

    def get_all_location_image():
        datas = _repo.get_all_location_image()
        return datas

    def get_all_location_point():
        datas = _repo.get_all_location()
        response = []
        for data in datas:
            response.append(ast.literal_eval(data.get('PointSpace')))
        return response

    def get_info_location_by_id(gmail: str):
        response = _repo.get_info_location_by_id(gmail)
        return response

    def update_info_location(data: _location_schemas.LocationUpdate):
        response = _repo.update_info(data)
        return response

    def get_main_info_location():
        datas = _repo.get_all_location()
        response = []
        for data in datas:
            first_image = _repo.get_image_locatio_by_id(
                f'IMAGE#{data.get("IdLocation")}', f'IMAGE#{data.get("IdLocation")}').get('ListImage')[0]
            url_image = _s3.create_presigned_url(first_image)
            response.append({
                'Path': url_image,
                'TimeStar': data.get("TimeStar"),
                'InfoLocation': data.get("InfoLocation"),
                'NameLocation': data.get("NameLocation"),
                'Price': data.get("Price"),
                'IdLocation': data.get("IdLocation"),
            })
            if (len(response) == 4):
                break
        return response

    def get_main_info_location_all():
        datas = _repo.get_all_location()
        response = []
        for data in datas:
            first_image = _repo.get_image_locatio_by_id(
                f'IMAGE#{data.get("IdLocation")}', f'IMAGE#{data.get("IdLocation")}').get('ListImage')[0]
            url_image = _s3.create_presigned_url(first_image)
            response.append({
                'Path': url_image,
                'TimeStar': data.get("TimeStar"),
                'InfoLocation': data.get("InfoLocation"),
                'NameLocation': data.get("NameLocation"),
                'Price': data.get("Price"),
                'IdLocation': data.get("IdLocation"),
            })
        return response

    def get_info_by_id(data: _location_schemas.LocationDelete):
        location = _location.LocationEtity(**data.dict(by_alias=True))
        respon_location = _repo.get_location(location.pk, location.sk)
        url_image = _repo.get_image_locatio_by_id(
            f'IMAGE#{data.id_location}',
            f'IMAGE#{data.id_location}'
        ).get('ListImage')
        info_account = _repo.get_image_locatio_by_id(
            f'INFO#{respon_location.get("GmailBussiness")}',
            f'INFO#{respon_location.get("GmailBussiness")}'
        )
        i = 0
        list_image = [1]
        for item in url_image:
            i += 1
            list_image.append(_s3.create_presigned_url(item))
        response = {
            'ListImage': list_image,
            'Address': respon_location.get('Address'),
            'NameLocation': respon_location.get('NameLocation'),
            'Model': respon_location.get('Model'),
            'TimeStar': respon_location.get('TimeStar'),
            'InfoLocation': respon_location.get('InfoLocation'),
            'Price': respon_location.get('Price'),
            'PointAddress': ast.literal_eval(respon_location.get('PointAddress')),
            'PointSpace': ast.literal_eval(respon_location.get('PointSpace')),
            'PointCross': ast.literal_eval(respon_location.get('PointCross')),
            'FullName': info_account.get('FullName'),
            'Gmail': info_account.get('Gmail'),
            'SDT': info_account.get('Number'),
        }
        return response

    def get_info_list_id(data_in: list):
        response = []
        for data in data_in:
            respon_location = _repo.get_location(
                f'LOCATION#{data}', f'LOCATION#{data}')
            price = respon_location.get('Price').split('-')
            response.append({
                'NameLocation': respon_location.get('NameLocation'),
                'TimeStar': respon_location.get('TimeStar'),
                'IdLocation': respon_location.get('IdLocation'),
                'PriceMin': int(price[0]),
                'PriceMax': int(price[1]),
            })
        return response
