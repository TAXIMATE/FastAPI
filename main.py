
from fastapi import FastAPI, HTTPException, Depends, Request, Response
from pydantic import BaseModel
from typing import Optional, List, Any, Dict, Tuple, cast
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from db import models  
from db.crud import upsert_user, get_user
from db.crud import get_team, create_team, delete_team
from db.crud import get_all_tms, get_tm_list_by_station
from db.crud import create_comment, get_comment, get_all_comments, update_comment, delete_comment
from db.crud import create_temperature, get_temperature, get_all_temperatures, update_temperature, delete_temperature
from db.database import SessionLocal, get_db

from ouath import Oauth,CLIENT_ID, CLIENT_SECRET, REDIRECT_URI


app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://kauth.kakao.com",
    "https://kapi.kakao.com"
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

# kakao login
class User(BaseModel):
    access_token: str

class RefreshToken(BaseModel):
    refresh_token: str

class Settings(BaseModel):
    authjwt_secret_key: str = "I'M IML."
    authjwt_token_location: str = "cookies"
    authjwt_cookie_secure: bool = False
    authjwt_cookie_csrf_protect: bool = True
    authjwt_access_token_expires: int = 30
    authjwt_refresh_token_expires: int = 100


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


@app.get("/oauth", description="This API is used for oauth authorization. It gets the code as input, gets the user information, upserts the user, and creates and sets the access and refresh tokens.")
def oauth_api(code: str, Authorize: AuthJWT = Depends()):
    oauth = Oauth()
    auth_info = oauth.auth(code)
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    user = models.User(user)
    upsert_user(user)

    access_token = Authorize.create_access_token(subject=user.id)
    refresh_token = Authorize.create_refresh_token(subject=user.id)
    tokens = {"access_token": access_token, "refresh_token": refresh_token}
    Authorize.set_access_cookies(tokens)

    return tokens

@app.get("/token/refresh", description="This API is used to refresh the jwt access token. It requires a valid refresh token.")
def refresh_token(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}

@app.get("/token/remove", description="This API is used to remove jwt tokens. It unsets the jwt access and refresh cookies.")
def remove_token(response: Response, Authorize: AuthJWT = Depends()):
    Authorize.unset_jwt_cookies(response)
    return {"message": "Successfully removed tokens"}

@app.get("/userinfo", description="This API is used to get user information. It requires a valid jwt token and it returns the information of the user related to the token.")
def get_user_info(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    user_info = get_user(current_user).serialize()
    return user_info

@app.get("/oauth/url", description="This API is used to get the URL for the Kakao oauth service.")
def get_oauth_url():
    return JSONResponse(content={"kakao_oauth_url": "https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" % (CLIENT_ID, REDIRECT_URI)})

@app.post("/oauth/refresh", description="This API is used to refresh the oauth access token. It gets the refresh token as input and returns a new access token and refresh token.")
def refresh_oauth(refresh_token: RefreshToken):
    result = Oauth().refresh(refresh_token.refresh_token)
    return result

@app.post("/oauth/userinfo", description="This API is used to get user information from the Kakao oauth service. It requires a valid oauth access token and it returns the information of the user related to the token.")
def get_oauth_userinfo(user: User):
    result = Oauth().userinfo("Bearer " + user.access_token)
    return result

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

@app.get("/")
async def home():
    return {"hello":"world"}