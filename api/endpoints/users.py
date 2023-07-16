from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
# from sqlalchemy.orm import Session
# from db import crud, database, models

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

@router.get("/location/{user_id}")
async def get_location(user_id: int):
    # db: Session = Depends(get_db)
    # user = crud.get_user(db, user_id=user_id)
    # if user is None:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return Location(latitude=user.latitude, longitude=user.longitude)
    return {"message": f"Get request for user location {user_id}"}

@router.get("/tm_list/{station}")
async def get_tm_list(station: str):
    # db: Session = Depends(get_db)
    # tm_list = crud.get_tm_list_by_station(db, station=station)
    # return tm_list
    return {"message": f"Get request for tm list for station {station}"}

@router.put("/user_info/")
async def put_user_info(user: UserInfo):
    # db: Session = Depends(get_db)
    # updated_user = crud.update_user_info(db, user)
    # return {"status": "200 OK", "updated_user": updated_user}
    return {"message": "Put request received", "user": user}
