from app.models.domain import info as _domain_info
from app.models.domain import account as _domain_account


class InfoData(
    _domain_account.AccountGmail,
    _domain_info.InfoFullName,
    _domain_info.InfoCMND,
    _domain_info.InfoNumber,
    _domain_info.InfoPath
):
    pass


class InfoUpdate(
    _domain_info.InfoFullName,
    _domain_info.InfoCMND,
    _domain_info.InfoNumber
):
    pass
