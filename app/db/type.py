from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


class TypeRepositories():

    def create_type(
        self,
        type_in: dict
    ):
        try:
            response = helpers.put_item_not_exists_PK_And_SK(type_in)
            return response
        except Exception:
            report_status.create_exception("Type")

    def delete_type(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_type(self) -> list:
        try:
            all_type = table.scan(
                FilterExpression=Attr('PK').begins_with('TYPE#')
            )
            return all_type['Items']
        except Exception:
            _ = report_status.get_exception("Type")
