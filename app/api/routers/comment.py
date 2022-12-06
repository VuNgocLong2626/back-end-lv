from fastapi import APIRouter
from app.models.schemas import comment as _schemas_comment
from app.services.comment import commentService
from typing import List


router = APIRouter()


@router.post('/create-comment')
async def create_comment(comment_in: _schemas_comment.CommentIn):
    response = commentService.create_comment(comment_in)
    return response


@router.get("/get-all-comment")
async def get_all():
    response = commentService.get_all_all()
    return response


@router.post("/get-all-comment-location")
async def get_all(data: _schemas_comment.CommentAllLocation):
    response = commentService.get_all_comment_location(data)
    return response


@router.post('/delete-comment')
async def delete_comment(per_in: _schemas_comment.CommentInDelete):
    response = commentService.delete_comment(per_in)
    return response
