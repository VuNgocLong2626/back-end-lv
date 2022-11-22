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
from ksuid import Ksuid
from datetime import timedelta, datetime


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
        time_rep = timedelta(hours=3)

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
            },
            expires_delta=time_rep
        )
        response = {
            "AccessToken": access_token,
            "TokenType": "bearer",
            "Expire": time_rep + datetime.utcnow(),
            "gmail": account_in.gmail
        }

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
        time_rep = timedelta(hours=3)

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
            },
            expires_delta=time_rep
        )
        response = {
            "AccessToken": access_token,
            "TokenType": "bearer",
            "Expire": time_rep + datetime.utcnow(),
            "gmail": account_in.gmail
        }

        return response

    def register(
        user_in: _account_schemas.AccountRegister,
        path: UploadFile
    ) -> None:

        account = _account.AccountEtity(**user_in.dict(by_alias=True))
        info = _info.InfoEtity(**user_in.dict(by_alias=True))
        time_rep = timedelta(hours=2)
        _ = _repo_info.create_info(info.dict(by_alias=True))
        _ = _repo.create_account(account.dict(by_alias=True))
        _ = _s3.upload_file(path, info.path)
        access_token = _auth.create_access_token(
            data={
                "gmail": account.gmail,
                "permission": account.permission,
            },
            expires_delta=time_rep
        )
        response = {
            "AccessToken": access_token,
            "TokenType": "bearer",
            "Expire": time_rep + datetime.utcnow(),
            "gmail": user_in.gmail

        }
        return response

    def delete_account(
        token_data: _account_schemas.AccountDelete
    ):
        user = _user.UserEtity(**token_data.dict(by_alias=True))
        info = _info.InfoEtity(**token_data.dict(by_alias=True))
        _ = _repo.delete_account(user.pk, user.sk)
        _ = _repo_info.delete_info(info.pk, info.sk)
        _ = _s3.delete_file(info.path)
        return {'message': 'delete successfully'}

    def change_password(
        password_in: _account_schemas.AccountPassword,
        user_in: _account_schemas.TokenData
    ):
        user_entity = _user.UserEtity(**user_in)
        user_res = _repo.get_account(user_entity.pk, user_entity.sk)
        user = _auth.verify_password(
            password_in.password_old, user_res.get('Password'))

        if not user and user_res:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Not Found User",
            )
        _ = _repo.change_password(
            user_entity.pk,
            user_entity.sk,
            _auth.get_password_hash(password_in.password)
        )

        return user_entity

    def get_info(
        user_in: _account_schemas.TokenData
    ):
        user_entity = _info.InfoEtity(**user_in)
        user_account = _user.UserEtity(**user_in)
        user_res = _repo.get_account(user_account.pk, user_account.sk)
        info_res = _repo_info.get_info(user_entity.pk, user_entity.sk)
        url_image = _s3.create_presigned_url(info_res.get('Path'))
        response = _info_schemas.InfoData(**info_res)
        setattr(response, 'path', url_image)
        setattr(response, 'permission', user_res.get('Permission'))
        return response

    def update_image(
        path: UploadFile,
        user_in: _account_schemas.TokenData
    ):
        user_entity = _info.InfoEtity(**user_in)
        info_res = _repo_info.get_info(user_entity.pk, user_entity.sk)
        file_name = _s3.get_file_name(path.filename, str(Ksuid()))
        _ = _repo_info.update_image(user_entity.pk, user_entity.sk, file_name)
        _ = _s3.delete_file(info_res.get('Path'))
        _ = _s3.upload_file(path, file_name)
        response = _s3.create_presigned_url(file_name)

        return response

    def update_info(
        info_in: _info_schemas.InfoUpdate,
        user_in: _account_schemas.TokenData
    ):
        user_entity = _info.InfoEtity(**user_in)
        _ = _repo_info.update_info(user_entity.pk, user_entity.sk, info_in)
        return {'message': 'delete successfully'}

    def get_all_info_account(permission: str):
        all_items = _repo.get_all_account()
        response = []
        if permission:
            for item in all_items:
                if item.get('Permission') == permission:
                    response.append(item)
            return response
        # for item in all_items:
        #     if
        return all_items
