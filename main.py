
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List, Any, Dict, Tuple, cast
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import models  # db 폴더가 상대경로에 있으면 이렇게 임포트
from db.crud import get_user, create_user, update_user, delete_user
from db.crud import get_team, create_team, delete_team
from db.crud import get_all_tms, get_tm_list_by_station
from db.crud import create_station, get_station, update_station, delete_station
from db.crud import create_comment, get_comment, get_all_comments, update_comment, delete_comment
from db.crud import create_temperature, get_temperature, get_all_temperatures, update_temperature, delete_temperature
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

CLIENT_ID = "198f75998f7dc4f1198f75970400f56"
CLIENT_SECRET = "3pdc4f1198f759Ey4yFPR24198f759ZzO"
REDIRECT_URI = "http://localhost:5000/oauth"



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

    tm_list = get_tm_list_by_station(db, station=station)
    if not tm_list:
        raise HTTPException(status_code=404, detail="No TMList found for this station")

    return tm_list


#2 Authentication


CLIENT_ID = "198f75998f7dc4f1198f75970400f56"
CLIENT_SECRET = "3pdc4f1198f759Ey4yFPR24198f759ZzO"
REDIRECT_URI = "http://localhost:5000/oauth"

@app.get("/oauth/url")
def oauth_url_api():
    return {
        "kakao_oauth_url": "https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
        % (CLIENT_ID, REDIRECT_URI)
    }


#3 CRUD Team
@app.get("/team/{team_no}", response_model=TeamInfo, description="Get specific team info by team id")
async def get_team_info(team_no: int, db: Session = Depends(get_db)):
    team = get_team(db, team_id=team_no)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@app.delete("/team/{team_no}", description="Delete a specific team by team id")
async def delete_team(team_no: int, db: Session = Depends(get_db)):
    team = get_team(db, team_id=team_no)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    delete_team(db, team_id=team_no)
    return {"message": f"Team {team_no} deleted successfully"}

@app.put("/team/", response_model=TeamInfo, description="Create a new team")
async def put_team_info(team: TeamInfo, db: Session = Depends(get_db)):
    new_team = create_team(db, team=team)
    return new_team


#4 Rating
@app.post("/rating/")
async def post_rating(rating: Rating):
    # db: Session = Depends(get_db)
    # 평점을 저장하는 코드를 여기에 작성합니다.
    # create_rating(db, rating=rating)
    return {"message": "Post request received", "rating": rating}