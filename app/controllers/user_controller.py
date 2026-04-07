from app.db import db
from app.models.user_model import user_helper
from bson import ObjectId, errors

collection = db["users"]

def is_valid_object_id(id: str):
    return ObjectId.is_valid(id)

async def create_user(user_data):
    result = await collection.insert_one(user_data)
    new_user = await collection.find_one({"_id": result.inserted_id})
    return user_helper(new_user)

async def get_users():
    users = []
    async for user in collection.find():
        users.append(user_helper(user))
    return users

async def get_user(user_id: str):
    if not is_valid_object_id(user_id):
        return None
    user = await collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(user) if user else None

async def update_user(user_id: str, data: dict):
    if not is_valid_object_id(user_id):
        return None
    await collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    return await get_user(user_id)

async def delete_user(user_id: str):
    if not is_valid_object_id(user_id):
        return False
    await collection.delete_one({"_id": ObjectId(user_id)})
    return True