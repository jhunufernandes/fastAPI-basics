from fastapi import APIRouter

# from app import crud, models, schemas


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Customers"}
