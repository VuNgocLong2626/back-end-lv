from fastapi import APIRouter
from app.models.schemas import feedback as _schemas_feedback
from app.services.feedback import FeedbackService
from typing import List


router = APIRouter()


@router.post('/create-feedback')
async def create_feedback(feedback_in: _schemas_feedback.FeedBackData):
    response = FeedbackService.create_feedback(feedback_in)
    return response


@router.get('/get-all-feedback', response_model=List[_schemas_feedback.FeedBackOut])
async def get_all():
    response = FeedbackService.get_all_feedback()
    return response


@router.delete('/delete-feedback')
async def delete_feedback(feedback_in: _schemas_feedback.FeedBackDelete):
    response = FeedbackService.delete_feedback(feedback_in)
    return response


@router.put('/update-display')
async def update_feedback(feedback_in: _schemas_feedback.FeedBackUpdate):
    response = FeedbackService.update_display(feedback_in)
    return response


@router.get('/get-all-true', response_model=List[_schemas_feedback.FeedBackOut])
async def get_all(display: bool):
    response = FeedbackService.get_all_display_true(display)
    return response


@router.get('/get-by_date', response_model=List[_schemas_feedback.FeedBackOut])
async def get_all(day: int):
    response = FeedbackService.get_by_date(day)
    return response
