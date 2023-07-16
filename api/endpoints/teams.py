from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

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
    # 팀 정보를 가져오는 코드를 여기에 작성합니다.
    pass

@router.delete("/team/{team_no}")
async def delete_team(team_no: int):
    # 팀을 삭제하는 코드를 여기에 작성합니다.
    pass

@router.put("/team/")
async def put_team_info(team: TeamInfo):
    # 팀 정보를 업데이트하는 코드를 여기에 작성합니다.
    pass

@router.post("/rating/")
async def post_rating(rating: Rating):
    # 평점을 저장하는 코드를 여기에 작성합니다.
    pass
