from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
def dashboard():
    return {"testing": "dashboard"}


@router.get("/dashboard/details")
def dashboard():
    return {"testing": "dashboard_details"}


@router.get("/dashboard/details/finerdetails")
def dashboard():
    return {"testing": "dashboard_details_finer"}