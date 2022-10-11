from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


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

    def get_account(
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
