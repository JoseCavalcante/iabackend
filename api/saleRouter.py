from fastapi import APIRouter

router = APIRouter()

@router.get("/api/sale/list")
async def list_sales():
    return "General list of sales"

@router.get("/api/sale/create")
async def create_sale():
    return "Create a sale"