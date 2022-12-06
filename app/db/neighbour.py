from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table
from app.models.schemas import neighbour as _neighbour_schemas


class neighbourRepositories():

    def create_neighbour(
        self,
        neighbour_in: dict
    ):
        try:
            response = helpers.put_item(neighbour_in)
            return response
        except Exception:
            report_status.create_exception("neighbour")

    def delete_neighbour(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_neighbour(
        self,
        pk: str,
        sk: str
    ):
        try:
            neighbour_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = neighbour_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Account")

    def get_all_neighbour(self) -> list:
        try:
            all_feedback = table.scan(
                FilterExpression=Attr('PK').begins_with('NEIGHBOUR#')
            )
            return all_feedback['Items']
        except Exception:
            _ = report_status.get_exception("Feedback")

    def update_list_address(
        self,
        pk: str,
        sk: str,
        path: list
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
                    '#pw': 'ListAddressNeighbour'
                }
            )
        except Exception:
            _ = report_status.get_exception("neighbour")

    def get_neighbour_star(
        self,
        pk: str,
        sk: str
    ):
        # try:
        neighbour_type = table.query(
            KeyConditionExpression=Key("PK").eq(pk) &
            Key("SK").eq(sk)
        )
        respon = neighbour_type["Items"][0]
        return respon
        # except Exception:
        #     _ = report_status.get_exception("Account")
    # def update_image(
    #     self,
    #     pk: str,
    #     sk: str,
    #     path: str
    # ) -> None:
    #     try:
    #         _ = table.update_item(
    #             Key={
    #                 'PK': pk,
    #                 'SK': sk
    #             },
    #             UpdateExpression='SET #pw = :val1',
    #             ExpressionAttributeValues={
    #                 ':val1': path,
    #             },
    #             ExpressionAttributeNames={
    #                 '#pw': 'Path'
    #             }
    #         )
    #     except Exception:
    #         _ = report_status.get_exception("neighbour")

    # def update_neighbour(
    #     self,
    #     pk: str,
    #     sk: str,
    #     neighbour: _neighbour_schemas.neighbourUpdate
    # ) -> None:
    #     try:
    #         _ = table.update_item(
    #             Key={
    #                 'PK': pk,
    #                 'SK': sk
    #             },
    #             UpdateExpression='SET #fn = :val1, #cm = :val2, #num = :val3,',
    #             ExpressionAttributeValues={
    #                 ':val1': neighbour.fullname,
    #                 ':val2': neighbour.cmnd,
    #                 ':val3': neighbour.number
    #             },
    #             ExpressionAttributeNames={
    #                 '#fn': 'FullName',
    #                 '#cm': 'CMND',
    #                 '#num': 'Number'
    #             }
    #         )
    #     except Exception:
    #         _ = report_status.get_exception("neighbour")
