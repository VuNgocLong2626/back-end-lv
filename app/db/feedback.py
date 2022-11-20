from app.utils import report_status
from app.utils.aws import helpers
from boto3.dynamodb.conditions import Attr, Key
from app.utils.aws.dynamodb import table
from datetime import date, timedelta


class FeedbackRepositories():

    def create_feedback(
        self,
        feedback_in: dict
    ):
        # try:
        response = helpers.put_item_not_exists_PK_And_SK(feedback_in)
        return response
        # except Exception:
        #     report_status.create_exception("Feedback")

    def delete_feedback(
        self,
        pk: str,
        sk: str
    ):
        _ = helpers.delete_item(pk, sk)

    def get_all_feedback(self) -> list:
        try:
            all_feedback = table.scan(
                FilterExpression=Attr('PK').begins_with('FEEDBACK#')
            )
            return all_feedback['Items']
        except Exception:
            _ = report_status.get_exception("Feedback")

    def update_display(
        self,
        pk: str,
        sk: str,
        display: str
    ) -> None:
        try:
            _ = table.update_item(
                Key={
                    'PK': pk,
                    'SK': sk
                },
                UpdateExpression='SET #pw = :val1',
                ExpressionAttributeValues={
                    ':val1': display,
                },
                ExpressionAttributeNames={
                    '#pw': 'Display'
                }
            )
        except Exception:
            _ = report_status.get_exception("Info")

    def get_all_display_true(self, display: bool) -> list:
        try:
            all_feedback = table.scan(
                FilterExpression=Attr('Display').eq(display)
            )
            return all_feedback['Items']
        except Exception:
            _ = report_status.get_exception("Feedback")

    def get_by_date(self, day: int):
        try:
            all_feedback = table.scan(
                FilterExpression=Attr('DateFeedback').between(
                    (date.today() - timedelta(days=day)).strftime('%Y-%m-%d'),
                    date.today().strftime('%Y-%m-%d')) and Attr('Display').eq(False)
            )
            return all_feedback['Items']
        except Exception:
            _ = report_status.get_exception("Feedback")
