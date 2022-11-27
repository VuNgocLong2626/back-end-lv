from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table
from app.models.schemas import info as _info_schemas
from app.models.schemas import location as _info_location


class LocationRepositories():

    def create_location(
        self,
        location_in: dict
    ):
        try:
            response = helpers.put_item(location_in)
            return response
        except Exception:
            report_status.create_exception("location")

    def delete_location(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_location(self) -> list:
        try:
            all_space = table.scan(
                FilterExpression=Attr('PK').begins_with('LOCATION#')
            )
            return all_space['Items']
        except Exception:
            _ = report_status.get_exception("space")

    def get_all_location_image(self) -> list:
        try:
            all_space = table.scan(
                FilterExpression=Attr('PK').begins_with('IMAGE#')
            )
            return all_space['Items']
        except Exception:
            _ = report_status.get_exception("space")

    def get_image_locatio_by_id(
        self,
        pk: str,
        sk: str
    ):
        try:
            location_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = location_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Account")

    def get_location(
        self,
        pk: str,
        sk: str
    ):
        try:
            location_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = location_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Account")

    def get_info_location_by_id(
        self,
        pk: str
    ):
        try:
            all_space = table.scan(
                FilterExpression=Attr('GmailBussiness').eq(pk)
            )
            return all_space['Items'][0]
        except Exception:
            _ = report_status.get_exception("space")

    def update_image(
        self,
        pk: str,
        sk: str,
        path: str
    ) -> None:
        try:
            _ = table.update_item(
                Key={
                    'PK': pk,
                    'SK': sk
                },
                UpdateExpression='SET #pw = :val1',
                ExpressionAttributeValues={
                    ':val1': path,
                },
                ExpressionAttributeNames={
                    '#pw': 'Path'
                }
            )
        except Exception:
            _ = report_status.get_exception("Info")

    def update_info(
        self,
        date: _info_location.LocationUpdate
    ) -> None:
        # try:
        _ = table.update_item(
            Key={
                'PK': date.pk,
                'SK': date.sk
            },
            UpdateExpression='SET #fn = :val1, #cm = :val2, #num = :val3, #info = :val4, #time = :val5, #model = :val6',
            ExpressionAttributeValues={
                ':val1': date.name_location,
                ':val2': date.Price,
                ':val3': date.address,
                ':val4': date.info_location,
                ':val5': date.time_star,
                ':val6': date.model,
            },
            ExpressionAttributeNames={
                '#fn': 'NameLocation',
                '#cm': 'Price',
                '#num': 'Address',
                '#info': 'InfoLocation',
                '#time': 'TimeStar',
                '#model': 'Model',
            }
        )
        # except Exception:
        #     _ = report_status.get_exception("Info")
