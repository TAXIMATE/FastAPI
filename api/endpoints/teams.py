from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
# from sqlalchemy.orm import Session
# from db import crud, database, models

router = APIRouter()

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

@router.get("/team/{team_no}")
async def get_team_info(team_no: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=team_no)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # return team
    return {"message": f"Get request for team information of {team_no}"}

@router.delete("/team/{team_no}")
async def delete_team(team_no: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=team_no)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # crud.delete_team(db, team_id=team_no)
    return {"message": f"Delete request for team {team_no}"}

@router.put("/team/")
async def put_team_info(team: TeamInfo):
    # db: Session = Depends(get_db)
    # new_team = crud.create_team(db, team=team)
    # return new_team
    return {"message": "Put request received", "team": team}

@router.post("/rating/")
async def post_rating(rating: Rating):
    # db: Session = Depends(get_db)
    # 평점을 저장하는 코드를 여기에 작성합니다.
    # crud.create_rating(db, rating=rating)
    return {"message": "Post request received", "rating": rating}

@router.get("/team/{teamNo}")
async def get_team_info(teamNo: int):
    # db: Session = Depends(get_db)
    # team = crud.get_team(db, team_id=teamNo)
    # if team is None:
    #     raise HTTPException(status_code=404, detail="Team not found")
    # return team
    return {"message": f"Get request for team {teamNo}"}
