from fastapi import APIRouter

router = APIRouter()

@router.get("/api/employer/list")
async def list_employer():
    return "General list of employer"

@router.get("/api/employer/create")
async def create_employer():
    return "Create a employer"