
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

from db import models  # db 폴더가 상대경로에 있으면 이렇게 임포트
from db.crud import get_user, get_users, create_user, update_user, delete_user
from db.crud import get_station, get_stations, create_station, update_station, delete_station
from db.crud import get_tm, get_tms, create_tm, update_tm, delete_tm
from db.crud import get_comment, get_comments, create_comment, update_comment, delete_comment
from db.crud import get_temperature, get_temperatures, create_temperature, update_temperature, delete_temperature
from db.database import SessionLocal, get_db

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

class TeamInfo(BaseModel):
    start_station: str
    end_station: str
    start_time: str
    current_population: int
    member_info: List[int]
    comments: Optional[str]

class Rating(BaseModel):
    team_no: int
    rating: float

#1 Landing Page
@app.get("/tm_list/{station}", response_model=List[TMList], description="Retrieve all TM lists related to the specified station")
async def get_tm_list(station: str, db: Session = Depends(get_db)):
    if not station:
        raise HTTPException(status_code=400, detail="Station must not be empty")

    tm_list = crud.get_tm_list_by_station(db, station=station)
    if not tm_list:
        raise HTTPException(status_code=404, detail="No TMList found for this station")

    return tm_list


#2 Authentication
@app.post("/kakaoAuthCode/")
async def kakao_auth(code: KakaoAuthCode):
    return {"auth_code": code.auth_code}


#3 CRUD Team
@app.get("/team/{team_no}", response_model=TeamInfo, description="Get specific team info by team id")
async def get_team_info(team_no: int, db: Session = Depends(get_db)):
    team = crud.get_team(db, team_id=team_no)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.delete("/team/{team_no}", description="Delete a specific team by team id")
async def delete_team(team_no: int, db: Session = Depends(get_db)):
    team = crud.get_team(db, team_id=team_no)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    crud.delete_team(db, team_id=team_no)
    return {"message": f"Team {team_no} deleted successfully"}

@app.put("/team/", response_model=TeamInfo, description="Create a new team")
async def put_team_info(team: TeamInfo, db: Session = Depends(get_db)):
    new_team = crud.create_team(db, team=team)
    return new_team


#4 Rating
@app.post("/rating/")
async def post_rating(rating: Rating):
    # db: Session = Depends(get_db)
    # 평점을 저장하는 코드를 여기에 작성합니다.
    # crud.create_rating(db, rating=rating)
    return {"message": "Post request received", "rating": rating}