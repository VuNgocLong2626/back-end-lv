from app.models.domain import contact as _domain_contact


class ContactIn(
    _domain_contact.ContactFullName,
    _domain_contact.ContactGmail,
    _domain_contact.ContactNumber,
    _domain_contact.ContactContent
):
    pass
