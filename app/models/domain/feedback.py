from pydantic import BaseModel, Field


class FeedbackFullname(BaseModel):
    fullname: str = Field(None, alias='Fullname')


class FeedbackGmail(BaseModel):
    gmail: str = Field(None, alias='Gamil')


class FeedbackMessage(BaseModel):
    message: str = Field(None, alias='Message')


class FeedbackNumber(BaseModel):
    number: str = Field(None, alias='Number')


class FeedbackDisplay(BaseModel):
    display: bool = Field(False, alias='Display')
