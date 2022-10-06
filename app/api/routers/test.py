from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_basic():
    respon = {
        "Name": "Long",
        "Age": 22
    }
    return respon
