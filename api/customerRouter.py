from fastapi import APIRouter


router = APIRouter()


@router.get("/api/customer/list")
async def listcustomer():
    return "List of customer"


@router.get("/api/customer/create")
async def createcustomer():
    return "Customer Created "


