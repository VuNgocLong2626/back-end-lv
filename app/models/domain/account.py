from pydantic import BaseModel, Field


class AccountGmail(BaseModel):
    gmail: str = Field(None, alias='Gmail')


class AccountPassword(BaseModel):
    password: str = Field(None, alias='Password')
