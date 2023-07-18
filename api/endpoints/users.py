from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
# import requests
import json
# from sqlalchemy.orm import Session
# from db import crud, database, models

router = APIRouter()

class TMList(BaseModel):
    start_station: str
    end_station: str
    desired_departure: str
    current_members: int

class KakaoAuthCode(BaseModel):
    auth_code: str

class KakaoUserInfo(BaseModel):
    nickname: str
    profile_image: str


# Dummy DB
user_db = {}

@router.get("/tm_list/{station}")
async def get_tm_list(station: str):
    # db: Session = Depends(get_db)
    # tm_list = crud.get_tm_list_by_station(db, station=station)
    # return tm_list
    return TMList

@router.post("/kakao_auth/")
async def kakao_auth(code: KakaoAuthCode):
    # Send POST request to Kakao login server
    # Assuming the URL and the parameters needed
   

    # Send profile picture and nickname back to the client
    return KakaoUserInfo(nickname=user_data["properties"]["nickname"], profile_image=user_data["properties"]["profile_image"])

