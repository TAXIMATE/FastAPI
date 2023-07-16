from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()  

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    profile_picture = Column(String)
    gender = Column(Boolean)

class Station(Base):
    __tablename__ = "stations"

    id = Column(Integer, primary_key=True, index=True)
    stations = Column(String)
    # 추가 필요한 역에 대한 속성들

class TM(Base):
    __tablename__ = "tms"

    id = Column(Integer, primary_key=True, index=True)
    start_station = Column(String, index=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    member_1 = Column(Integer, ForeignKey("users.id"))
    member_2 = Column(Integer, ForeignKey("users.id"))
    member_3 = Column(Integer, ForeignKey("users.id"))
    end_station = Column(String, index=True)
    desired_departure = Column(DateTime)
    comment = Column(String)
    in_progress = Column(Boolean)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    tm_id = Column(Integer, ForeignKey("tms.id"))
    timestamp = Column(DateTime)
    written_by = Column(Integer, ForeignKey("users.id"))

class Temperature(Base):
    __tablename__ = "temperatures"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tm_id = Column(Integer, ForeignKey("tms.id"))
    temperature = Column(Integer)  

