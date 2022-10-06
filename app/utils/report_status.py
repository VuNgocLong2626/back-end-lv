from fastapi import HTTPException, status


def get_exception(name: str):
    credentials_exception = HTTPException(
        detail=f"Not Found {name}",
        status_code=status.HTTP_404_NOT_FOUND,
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception


def get_done(name: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_200_OK,
        detail=f"Done {name}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception


def create_exception(name: str):
    credentials_exception = HTTPException(
        detail=f"Not Create {name}",
        status_code=status.HTTP_400_BAD_REQUEST,
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception


def delete_done(name: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_200_OK,
        detail=f"Delete Done {name}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception


def create_done(name: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_200_OK,
        detail=f"Create Done {name}",
        headers={"WWW-Authenticate": "Bearer"},
    )
    raise credentials_exception
