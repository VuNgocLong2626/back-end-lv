from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table


class CommentRepositories():

    def create_comment(
        self,
        comment_in: dict
    ):
        # try:
        response = helpers.put_item_not_exists_PK_And_SK(comment_in)
        return response
        # except Exception:
        #     report_status.create_exception("comment")

    def delete_comment(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_comment(
        self,
        gsi1pk: str,
    ) -> list:
        try:
            info_type = table.query(
                IndexName='GSI1',
                KeyConditionExpression=Key("GSI1PK").eq(gsi1pk)
            )
            respon = info_type["Items"]
            return respon
        except Exception:
            _ = report_status.get_exception("comment")

    def get_all_all(self) -> list:
        try:
            all_permission = table.scan(
                FilterExpression=Attr('PK').begins_with('COMMENT#')
            )
            return all_permission['Items']
        except Exception:
            _ = report_status.get_exception("Permission")
