from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate
from app.controllers import user_controller

router = APIRouter()

@router.post("/")
async def create(user: UserCreate):
    return await user_controller.create_user(user.dict())

@router.get("/")
async def get_all():
    return await user_controller.get_users()

@router.get("/{user_id}")
async def get_one(user_id: str):
    user = await user_controller.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}")
async def update(user_id: str, user: UserCreate):
    updated = await user_controller.update_user(user_id, user.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
async def delete(user_id: str):
    deleted = await user_controller.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}