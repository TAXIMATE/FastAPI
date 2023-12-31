from sqlalchemy.orm import Session
from db import models
from pydantic import schema


# 1 Landing
def get_tm_list_by_station(db: Session, station_name: str):
    station = db.query(models.Station).filter(models.Station.name == station_name).first()
    if not station:
        return None  # No station found with that name

    tm_list = []
    for team in station.teams:
        tm_list.append(
            {
                "start_station": team.start_station.name,
                "end_station": team.end_station.name,  # Similar relationship with end station
                "desired_departure": team.desired_departure,
                "current_members": team.current_members,
            }
        )
    return tm_list


# 2 Authentication
def get_user_by_kakao_auth_id(db: Session, auth_id: str):
    return db.query(models.User).filter(models.User.auth_id == auth_id).first()

def create_or_update_kakao_user(db: Session, user_info: dict):
    user = get_user_by_kakao_auth_id(db, user_info['id'])
    if user is None:
        user = models.User(
            nickname=user_info['properties']['nickname'],
            profile=user_info['properties']['profile_image'],
            thumbnail=user_info['properties']['thumbnail_image'],
            auth_id=user_info['id']
        )
        db.add(user)
    else:
        user.nickname = user_info['properties']['nickname']
        user.profile = user_info['properties']['profile_image']
        user.thumbnail = user_info['properties']['thumbnail_image']
    
    db.commit()
    db.refresh(user)
    return user



# 3 CRUD Team
def get_team(db: Session, team_id: int):
    return db.query(models.TM).filter(models.TM.id == team_id).first()


def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if db_team is None:
        return None
    db.delete(db_team)
    db.commit()
    return db_team


def create_team(db: Session, team: models.TM):
    db_team = models.TM(
        start_station=team.start_station,
        end_station=team.end_station,
        desired_departure=team.start_time,
        team_leader=team.member_info[0],
        member_1=team.member_info[1] if len(team.member_info) > 1 else None,
        member_2=team.member_info[2] if len(team.member_info) > 2 else None,
        member_3=team.member_info[3] if len(team.member_info) > 3 else None,
        comment=team.comments,
        in_progress=True,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


# For the Comment model
def create_comment(db: Session, comment: models.Comment):
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


def get_all_comments(db: Session):
    return db.query(models.Comment).all()


def update_comment(db: Session, comment: models.Comment):
    db_comment = get_comment(db, comment.id)
    if db_comment is None:
        return None
    for var, value in vars(comment).items():
        setattr(db_comment, var, value)
    db.commit()
    return db_comment


def delete_comment(db: Session, comment_id: int):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        return None
    db.delete(db_comment)
    db.commit()
    return db_comment


# For the Temperature model
def create_temperature(db: Session, temperature: models.Temperature):
    db.add(temperature)
    db.commit()
    db.refresh(temperature)
    return temperature


def get_temperature(db: Session, temperature_id: int):
    return (
        db.query(models.Temperature)
        .filter(models.Temperature.id == temperature_id)
        .first()
    )


def get_all_temperatures(db: Session):
    return db.query(models.Temperature).all()


def update_temperature(db: Session, temperature: models.Temperature):
    db_temperature = get_temperature(db, temperature.id)
    if db_temperature is None:
        return None
    for var, value in vars(temperature).items():
        setattr(db_temperature, var, value)
    db.commit()
    return db_temperature


def delete_temperature(db: Session, temperature_id: int):
    db_temperature = get_temperature(db, temperature_id)
    if db_temperature is None:
        return None
    db.delete(db_temperature)
    db.commit()
    return db_temperature
