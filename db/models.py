from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

#Authentication
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    profile = Column(String, unique=True, index=True)
    thumbnail = Column(String)
    auth_id = Column(String, unique=True)  # 카카오 사용자 고유 ID

#current team list
class Station(Base):
    __tablename__ = 'stations'  # 테이블 이름 수정
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    teams = relationship('Team', back_populates='start_station')


class Team(Base):
    __tablename__ = "teams"  # 테이블 이름 수정
    id = Column(Integer, primary_key=True, index=True)
    start_station_id = Column(Integer, ForeignKey('stations.id'), nullable=False)
    end_station = Column(String, index=True)
    desired_departure = Column(DateTime)
    comment = Column(String)
    in_progress = Column(Boolean)
    start_station = relationship('Station', back_populates='teams')
    comments = relationship('Comment', back_populates='team')  # Comment와의 관계 설정

#real time comment
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"))  # ForeignKey 수정
    timestamp = Column(DateTime)
    written_by = Column(Integer, ForeignKey("users.id"))
    team = relationship('Team', back_populates='comments')  # Team과의 관계 설정

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)

class Temperature(Base):
    __tablename__ = "temperatures"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    team_id = Column(Integer, ForeignKey("teams.id"))  # 여기도 수정
    temperature = Column(Integer)

