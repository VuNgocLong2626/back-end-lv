from app.models.schemas import feedback as _feedback_domain
from app.db.entity import feedback as _feedback

from app.db.feedback import FeedbackRepositories


_repo = FeedbackRepositories()


class FeedbackService():

    def create_feedback(
        feedback_in: _feedback_domain.FeedBackData
    ):
        entity = _feedback.FeedbackEtity(**feedback_in.dict(by_alias=True))
        _ = _repo.create_feedback(entity.dict(by_alias=True))
        return {'message': 'create successfully'}

    def delete_feedback(
        feedback_in: _feedback_domain.FeedBackDelete
    ):
        entity = _feedback.FeedbackEtity(**feedback_in.dict(by_alias=True))
        _ = _repo.delete_feedback(entity.pk, entity.sk)
        return {'message': 'delete successfully'}

    def get_all_feedback():
        response = _repo.get_all_feedback()
        return response

    def update_display(
        feedback_in: _feedback_domain.FeedBackUpdate
    ):
        entity = _feedback.FeedbackEtity(**feedback_in.dict(by_alias=True))
        _ = _repo.update_display(entity.pk, entity.sk, entity.display)
        return {'message': 'update successfully'}

    def get_all_display_true():
        response = _repo.get_all_display_true()
        return response
