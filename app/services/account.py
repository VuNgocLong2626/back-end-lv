from fastapi import HTTPException, status, UploadFile
from app.utils import report_status
from app.utils import auth as _auth
from app.models.schemas import account as _account_schemas
from app.models.schemas import info as _info_schemas

from app.db.account import AccountRepositories
from app.db.info import InfoRepositories

from app.db.entity import account as _account
from app.db.entity import user as _user
from app.db.entity import info as _info

from app.utils.aws import s3 as _s3


_repo = AccountRepositories()
_repo_info = InfoRepositories()


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

        if user_res.get('Permission') == 'Admin':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are Admin",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not user and user_res:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = _auth.create_access_token(
            data={
                "gmail": account_in.gmail,
                "permission": user_res.get('Permission')
            }
        )
        response = {"AccessToken": access_token, "TokenType": "bearer"}

        return response

    def login_API(
        account_in: _account_schemas.AccountIn
    ) -> None:
        user_data = _account_schemas.TokenData(**{
            'Gmail': account_in.gmail
        })
        user_entity = _user.UserEtity(**user_data.dict(by_alias=True))
        user_res = _repo.get_account(user_entity.pk, user_entity.sk)
        user = _auth.verify_password(
            account_in.password, user_res.get('Password'))

        if user_res.get('Permission') == 'Businesses':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="You are Businesses",
                headers={"WWW-Authenticate": "Bearer"},
            )



        if not user and user_res:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = _auth.create_access_token(
            data={
                "gmail": account_in.gmail,
                "permission": user_res.get('Permission')
            }
        )
        response = {"AccessToken": access_token, "TokenType": "bearer"}

        return response

    def register(
        user_in: _account_schemas.AccountRegister,
        path: UploadFile
    ) -> None:

        account = _account.AccountEtity(**user_in.dict(by_alias=True))
        info = _info.InfoEtity(**user_in.dict(by_alias=True))
        _ = _repo_info.create_info(info.dict(by_alias=True))
        _ = _repo.create_account(account.dict(by_alias=True))
        _ = _s3.upload_file(path, info.path)
        access_token = _auth.create_access_token(
            data={
                "gmail": account.gmail,
                "permission": account.permission
            }
        )
        response = {"AccessToken": access_token, "TokenType": "bearer"}
        return response

    def delete_account(
        token_data: _account_schemas.AccountDelete
    ):
        user = _user.UserEtity(**token_data.dict(by_alias=True))
        info = _info.InfoEtity(**token_data.dict(by_alias=True))
        _ = _repo.delete_account(user.pk, user.sk)
        _ = _repo_info.delete_info(info.pk, info.sk)
        return {'message': 'delete successfully'}
