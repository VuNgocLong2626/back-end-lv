from pydantic import BaseModel, Field
from app.models.domain import account as _domain_account
from app.models.domain import info as _domain_info


class AccountIn(
    _domain_account.AccountGmail,
    _domain_account.AccountPassword
):
    pass


class Token(BaseModel):
    access_token: str = Field(alias='AccessToken')
    token_type: str = Field(alias='TokenType')


class TokenData(
    _domain_account.AccountGmail
):
    pass


class AccountRegister(
    _domain_account.AccountGmail,
    _domain_account.AccountPassword,
    _domain_info.InfoFullName,
    _domain_info.InfoCMND,
    _domain_info.InfoNumber,
    _domain_info.InfoPath
):
    pass


class AccountDelete(
    _domain_account.AccountGmail
):
    pass
