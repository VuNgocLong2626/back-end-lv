from app.models.domain import feedback as _feedback_domain


class FeedBackData(
    _feedback_domain.FeedbackNumber,
    _feedback_domain.FeedbackFullname,
    _feedback_domain.FeedbackGmail,
    _feedback_domain.FeedbackMessage
):
    pass


class FeedBackDelete(
    _feedback_domain.FeedbackNumber
):
    pass


class FeedBackOut(
    _feedback_domain.FeedbackNumber,
    _feedback_domain.FeedbackFullname,
    _feedback_domain.FeedbackGmail,
    _feedback_domain.FeedbackMessage,
    _feedback_domain.FeedbackDate,
    _feedback_domain.FeedbackDisplay
):
    pass


class FeedBackUpdate(
    _feedback_domain.FeedbackNumber,
    _feedback_domain.FeedbackDisplay
):
    pass
