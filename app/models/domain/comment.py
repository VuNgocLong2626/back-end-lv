from pydantic import BaseModel, Field
from datetime import date


class CommentFullName(BaseModel):
    fullname: str = Field(None, alias='FullName')


class CommentComment(BaseModel):
    comment: str = Field(None, alias='Comment')


class CommentSDT(BaseModel):
    sdt: str = Field(None, alias='SDT')


class CommentStar(BaseModel):
    star: str = Field(None, alias='Star')


class CommentDate(BaseModel):
    date_comment: str = Field(date.today().__str__(), alias='DateComment')


class CommentStatus(BaseModel):
    status: bool = Field(False, alias='Status')
