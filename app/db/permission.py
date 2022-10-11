from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


class PermissionRepositories():

    def create_permission(
        self,
        permission_in: dict
    ):
        try:
            response = helpers.put_item_not_exists_PK_And_SK(permission_in)
            return response
        except Exception:
            report_status.create_exception("Permission")

    def delete_permission(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_perrmission(self) -> list:
        try:
            all_permission = table.scan(
                FilterExpression=Attr('PK').begins_with('PERMISSION#')
            )
            return all_permission['Items']
        except Exception:
            _ = report_status.get_exception("Permission")
