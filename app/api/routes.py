from fastapi import APIRouter

from app.api.endpoints import contacts, customers, users


api_router = APIRouter()

# api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(users.router, prefix="/users")
api_router.include_router(contacts.router, prefix="/contacts")
api_router.include_router(customers.router, prefix="/customers")
