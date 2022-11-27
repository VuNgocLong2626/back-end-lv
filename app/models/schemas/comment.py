from app.models.domain import comment as _domain_comment
from app.models.domain import base as _domain_base
from app.models.domain import location as _domain_location


class CommentIn(
    _domain_base.IdLocation,
    _domain_comment.CommentComment,
    _domain_comment.CommentFullName,
    _domain_comment.CommentStar,
    _domain_comment.CommentSDT
):
    pass


class CommentInData(
    _domain_base.IdLocation,
    _domain_base.IdComment,
    _domain_comment.CommentComment,
    _domain_comment.CommentFullName,
    _domain_comment.CommentStar,
    _domain_comment.CommentSDT,
    _domain_comment.CommentDate,
    _domain_comment.CommentStatus
):
    pass


class CommentInDelete(
    _domain_base.IdComment,
):
    pass


class CommentAllLocation(
    _domain_base.IdLocation
):
    pass
