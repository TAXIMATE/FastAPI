from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter()

class TMList(BaseModel):
    start_station: str
    end_station: str
    desired_departure: str
    current_members: int

class UserInfo(BaseModel):
    name: str
    age: int

class Location(BaseModel):
    latitude: float
    longitude: float

class AuthCode(BaseModel):
    auth_code: str

@router.get("/location/{user_id}")
async def get_location(user_id: int):
    return {"message": f"Get request for user location {user_id}"}

@router.get("/tm_list/{station}")
async def get_tm_list(station: str):
    return {"message": f"Get request for tm list for station {station}"}

@router.post("/")
async def post_auth_code(code: AuthCode):
    return {"auth_code": code.auth_code}
