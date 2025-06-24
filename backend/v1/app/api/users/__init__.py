from fastapi import APIRouter

from backend.v1.app.api.users.users import router as users_router


router = APIRouter()

router.include_router(users_router)
