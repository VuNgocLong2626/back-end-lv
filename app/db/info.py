from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table
from app.models.schemas import info as _info_schemas


class InfoRepositories():

    def create_info(
        self,
        info_in: dict
    ):
        try:
            response = helpers.put_item(info_in)
            return response
        except Exception:
            report_status.create_exception("Info")

    def delete_info(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_info(
        self,
        pk: str,
        sk: str
    ):
        try:
            info_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = info_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Account")

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
        pk: str,
        sk: str,
        info: _info_schemas.InfoUpdate
    ) -> None:
        try:
            _ = table.update_item(
                Key={
                    'PK': pk,
                    'SK': sk
                },
                UpdateExpression='SET #fn = :val1, #cm = :val2, #num = :val3,',
                ExpressionAttributeValues={
                    ':val1': info.fullname,
                    ':val2': info.cmnd,
                    ':val3': info.number
                },
                ExpressionAttributeNames={
                    '#fn': 'FullName',
                    '#cm': 'CMND',
                    '#num': 'Number'
                }
            )
        except Exception:
            _ = report_status.get_exception("Info")
