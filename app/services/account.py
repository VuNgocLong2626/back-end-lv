from fastapi import HTTPException, status
from app.utils import report_status
from app.utils import auth as _auth
from app.models.schemas import account as _account_schemas
from app.db.account import TypeRepositories
from app.db.entity import account as _account
from app.db.entity import user as _user

account_db = {
    "Password": "$2b$12$mvzf.2e1BXHxT8k6flbX1.Okthj7pBcAZywKCpPGogsGOPiBQc1Vy",
    "Gmail": "string"
}

_repo = TypeRepositories()


class AccountService():

    def login(
        account_in: _account_schemas.AccountIn
    ) -> None:
        user_data = _account_schemas.TokenData(**{
            'Gmail': account_in.gmail
        })
        user_entity = _user.UserEtity(**user_data.dict(by_alias=True))
        user_res = _repo.get_account(user_entity.pk, user_entity.sk)
        user = _auth.verify_password(
            account_in.password, user_res.get('Password'))

        if not user and user_res:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = _auth.create_access_token(
            data={"gmail": account_in.gmail})
        response = {"AccessToken": access_token, "TokenType": "bearer"}

        return response

    def register(
        user_in: _account_schemas.AccountRegister
    ) -> None:

        account = _account.AccountEtity(**user_in.dict(by_alias=True))
        _ = _repo.create_account(account.dict(by_alias=True))

        access_token = _auth.create_access_token(
            data={"gmail": account.gmail}
        )
        response = {"AccessToken": access_token, "TokenType": "bearer"}
        return response

    def delete_account(
        token_data: _account_schemas.AccountDelete
    ):
        user = _user.UserEtity(**token_data)
        _ = _repo.delete_account(user.pk, user.sk)
        return {'message': 'delete successfully'}
