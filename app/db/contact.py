from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table
from app.models.schemas import contact as _contact_schemas


class contactRepositories():

    def create_contact(
        self,
        contact_in: dict
    ):
        try:
            response = helpers.put_item(contact_in)
            return response
        except Exception:
            report_status.create_exception("contact")

    def delete_contact(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_contact(
        self,
        pk: str,
        sk: str
    ):
        try:
            contact_type = table.query(
                KeyConditionExpression=Key("PK").eq(pk) &
                Key("SK").eq(sk)
            )
            respon = contact_type["Items"][0]
            return respon
        except Exception:
            _ = report_status.get_exception("Account")

    def get_all_contact(self) -> list:
        try:
            all_feedback = table.scan(
                FilterExpression=Attr('PK').begins_with('CONTACT#')
            )
            return all_feedback['Items']
        except Exception:
            _ = report_status.get_exception("Feedback")

    # def update_contact(
    #     self,
    #     pk: str,
    #     sk: str,
    #     contact: _contact_schemas.contactUpdate
    # ) -> None:
    #     try:
    #         _ = table.update_item(
    #             Key={
    #                 'PK': pk,
    #                 'SK': sk
    #             },
    #             UpdateExpression='SET #fn = :val1, #cm = :val2, #num = :val3,',
    #             ExpressionAttributeValues={
    #                 ':val1': contact.fullname,
    #                 ':val2': contact.cmnd,
    #                 ':val3': contact.number
    #             },
    #             ExpressionAttributeNames={
    #                 '#fn': 'FullName',
    #                 '#cm': 'CMND',
    #                 '#num': 'Number'
    #             }
    #         )
    #     except Exception:
    #         _ = report_status.get_exception("contact")
