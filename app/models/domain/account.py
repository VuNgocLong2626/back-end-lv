from pydantic import BaseModel, Field


class AccountGmail(BaseModel):
    gmail: str = Field(alias='Gmail')


class AccountPassword(BaseModel):
    password: str = Field(alias='Password')
