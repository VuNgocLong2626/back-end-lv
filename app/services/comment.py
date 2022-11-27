from app.models.schemas import comment as _comment_schemas
from app.db.entity import comment as _comment

from app.db.comment import CommentRepositories


_repo = CommentRepositories()


class commentService():

    def create_comment(comment_in: _comment_schemas.CommentIn):
        comment = _comment.CommentEtity(
            **comment_in.dict(by_alias=True)
        )
        _ = _repo.create_comment(comment.dict(by_alias=True))
        return comment

    def get_all_all():
        response = _repo.get_all_all()
        return response

    def delete_comment(comment_in: _comment_schemas.CommentInDelete):
        comment = _comment.CommentEtity(
            **comment_in.dict(by_alias=True)
        )
        # return comment
        _ = _repo.delete_comment(comment.pk, comment.sk)
        return {'message': 'delete successfully'}

    def get_all_comment_location(comment_in: _comment_schemas.CommentAllLocation):
        comment = _comment.CommentEtity(
            **comment_in.dict(by_alias=True))
        response = _repo.get_all_comment(comment.gsi1pk)
        return response
