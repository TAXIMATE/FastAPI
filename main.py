
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

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
    member_info: list
    comments: Optional[str]

class Rating(BaseModel):
    team_no: int
    rating: float

@app.get("/tm_list/{station}")
async def get_tm_list(station: str):
    # db: Session = Depends(get_db)
    # tm_list = crud.get_tm_list_by_station(db, station=station)
    # return tm_list
    return TMList

@app.post("/kakaoAuthCode/")
async def kakao_auth(code: KakaoAuthCode):
    return {"auth_code": code.auth_code}

@app.get("/team/{team_no}")
async def get_team_info(team_no: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=team_no)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # return team
    return {"message": f"Get request for team information of {team_no}"}

@app.delete("/team/{team_no}")
async def delete_team(team_no: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=team_no)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # crud.delete_team(db, team_id=team_no)
    return {"message": f"Delete request for team {team_no}"}

@app.put("/team/")
async def put_team_info(team: TeamInfo):
    # db: Session = Depends(get_db)
    # new_team = crud.create_team(db, team=team)
    # return new_team
    return {"message": "Put request received", "team": team}

@app.post("/rating/")
async def post_rating(rating: Rating):
    # db: Session = Depends(get_db)
    # 평점을 저장하는 코드를 여기에 작성합니다.
    # crud.create_rating(db, rating=rating)
    return {"message": "Post request received", "rating": rating}

@app.get("/team/{teamNo}")
async def get_team_info(teamNo: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=teamNo)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # return team
    return {"message": f"Get request for team {teamNo}"}

@app.get("/")
def root():
    return {'Hello' : 'World!'}