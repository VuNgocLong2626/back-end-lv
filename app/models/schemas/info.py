from app.models.domain import info as _domain_info
from app.models.domain import account as _domain_account
from app.models.domain import permission as _domain_permission


class InfoData(
    _domain_account.AccountGmail,
    _domain_info.InfoFullName,
    _domain_info.InfoCMND,
    _domain_info.InfoNumber,
    _domain_info.InfoPath,
    _domain_permission.PermissionName
):
    pass


class InfoUpdate(
    _domain_info.InfoFullName,
    _domain_info.InfoCMND,
    _domain_info.InfoNumber
):
    pass
