from fastapi import APIRouter

router = APIRouter()

@router.get("/api/customer/list")
async def list_custumer():
    return "General list of customers"

@router.get("/api/customer/create")
async def create_custumer():
    return "Create a customer"

