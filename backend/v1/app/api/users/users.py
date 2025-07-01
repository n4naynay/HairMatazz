from fastapi import APIRouter, Body

from backend.v1.app.models.users.users import UserCreate

router = APIRouter()

table={}


@router.get("/dashboard")
def dashboard():
    return {"testing": "dashboard"}


@router.get("/dashboard/details")
def dashboard():
    return {"testing": "dashboard_details"}


@router.get("/dashboard/details/finerdetails")
def dashboard():
    return {"testing": "dashboard_details_finer"}


@router.post("/register-user", response_model=UserCreate, tags=["users"])
async def register_user(
        new_user: UserCreate = Body(..., embed=True)
):
    print(new_user)
    table[new_user.username] = new_user
    print(table)
    return new_user
