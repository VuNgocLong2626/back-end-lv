from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.security import OAuth2PasswordRequestForm
from app.models.schemas import account as _schemas_account
from app.services.account import AccountService
from app.utils import auth as _auth


router = APIRouter()


@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    data = {
        'Gmail': form_data.username,
        'Password': form_data.password
    }
    da = _schemas_account.AccountIn(**data)
    response = AccountService.login(da)
    return response


@router.get("/users/me/")
async def read_users_me(current_user: _schemas_account.AccountIn = Depends(_auth.get_current_user)):
    return current_user


@router.post("/register")
async def create_account(
    path: UploadFile = File(..., alias='Path'),
    number: str = Form(..., alias='Number'),
    cmnd: int = Form(..., alias='CMND'),
    fullname: str = Form(..., alias='FullName'),
    password: str = Form(..., alias='Password'),
    gmail: str = Form(..., alias='Gmail')
):
    user_in = _schemas_account.AccountRegister(**{
        'Number': number,
        'CMND': cmnd,
        'FullName': fullname,
        'Password': password,
        'Gmail': gmail,
        'Path': path.filename
    })
    response = AccountService.register(user_in, path)
    return response


@router.delete("/delete-account")
async def create_account(
    user: _schemas_account.AccountDelete,
    # user_in: _schemas_account.TokenData = Depends(_auth.get_current_user)
):
    response = AccountService.delete_account(user)
    return response
