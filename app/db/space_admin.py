from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


class SpaceRepositories():

    def create_space(
        self,
        space_in: dict
    ):
        # try:
        response = helpers.put_item_not_exists_PK_And_SK(space_in)
        return response
        # except Exception:
        #     report_status.create_exception("space")

    def delete_space(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_space(self) -> list:
        try:
            all_space = table.scan(
                FilterExpression=Attr('GSI2SK').begins_with('SPACE#')
            )
            return all_space['Items']
        except Exception:
            _ = report_status.get_exception("space")
