import csv
import random
from datetime import datetime
from sqlalchemy.orm import Session
from db_session import engine, get_new_session
from models import Station, Team
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

stations_csv_path = os.path.join(current_dir, 'stations.csv')

def insert_stations(db: Session):
    with open(stations_csv_path, 'r', encoding='utf-8') as file:
        for line in file:
            station_name = line.strip()
            station = Station(name=station_name)
            db.add(station)
        db.commit()

def insert_teams(db: Session):
    for _ in range(30):
        team = Team(
            start_station_id=random.randint(1, 100),  # 실제 station id 범위에 맞게 변경
            end_station="서울역",
            desired_departure=datetime.now(),  # 현재 시간 또는 원하는 시간으로 설정
            comment="이것은 코멘트입니다.",
            in_progress=random.choice([True, False])
        )
        db.add(team)
    db.commit()

db = get_new_session()

insert_stations(db)
insert_teams(db)  # 팀을 삽입하는 코드 실행
