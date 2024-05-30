from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_version():
    return {"version": "1.0.0"}
