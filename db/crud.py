from sqlalchemy.orm import Session
from db import models

# For the User model
def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user: models.User):
    db_user = get_user(db, user.id)
    if db_user is None:
        return None
    for var, value in vars(user).items():
        setattr(db_user, var, value)
    db.commit()
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# Similar CRUD operations can be written for Station, TM, Comment, Temperature models.
# Replace `user` with `station`, `tm`, `comment`, or `temperature` accordingly.

# For example, for Station model:

def create_station(db: Session, station: models.Station):
    db.add(station)
    db.commit()
    db.refresh(station)
    return station

def get_station(db: Session, station_id: int):
    return db.query(models.Station).filter(models.Station.id == station_id).first()

def update_station(db: Session, station: models.Station):
    db_station = get_station(db, station.id)
    if db_station is None:
        return None
    for var, value in vars(station).items():
        setattr(db_station, var, value)
    db.commit()
    return db_station

def delete_station(db: Session, station_id: int):
    db_station = get_station(db, station_id)
    if db_station is None:
        return None
    db.delete(db_station)
    db.commit()
    return db_station


# For the TM model
def create_tm(db: Session, tm: models.TM):
    db.add(tm)
    db.commit()
    db.refresh(tm)
    return tm

def get_tm(db: Session, tm_id: int):
    return db.query(models.TM).filter(models.TM.id == tm_id).first()

def get_all_tms(db: Session):
    return db.query(models.TM).all()

def update_tm(db: Session, tm: models.TM):
    db_tm = get_tm(db, tm.id)
    if db_tm is None:
        return None
    for var, value in vars(tm).items():
        setattr(db_tm, var, value)
    db.commit()
    return db_tm

def delete_tm(db: Session, tm_id: int):
    db_tm = get_tm(db, tm_id)
    if db_tm is None:
        return None
    db.delete(db_tm)
    db.commit()
    return db_tm

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
    return db.query(models.Temperature).filter(models.Temperature.id == temperature_id).first()

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
