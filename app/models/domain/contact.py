from pydantic import BaseModel, Field


class ContactFullName(BaseModel):
    fullname: str = Field(None, alias='FullName')


class ContactGmail(BaseModel):
    gmail: str = Field(None, alias='Gmail')


class ContactNumber(BaseModel):
    number: str = Field(None, alias='Number')


class ContactContent(BaseModel):
    content: str = Field(None, alias='Content')
