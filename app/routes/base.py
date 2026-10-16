from fastapi import APIRouter
from app.routes.get_students import router as get_router
from app.routes.create_students import router as create_router
from app.routes.update_students import router as update_router
from app.routes.delete_students import router as delete_router

#api router
api_router = APIRouter()
api_router.include_router(get_router)
api_router.include_router(create_router)
api_router.include_router(update_router)

api_router.include_router(delete_router)