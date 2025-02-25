from fastapi import APIRouter


router = APIRouter()


@router.get("/api/employee/list")
async def listemployee():
    return "list of employee"

@router.get("/api/employee/create")
async def createemployee():
    return "Employee created with succes"