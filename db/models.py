from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base()  

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, unique=True, index=True)
    profile = Column(String, unique=True, index=True)
    thumbnail = Column(String)

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

    @property
    def current_members(self):
        members = [self.team_leader, self.member_1, self.member_2, self.member_3]
        return len([member for member in members if member is not None])

class TeamInfo(Base):
    start_station: str
    end_station: str
    start_time: str
    member_info: List[str]
    comments: Optional[str] = None


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

