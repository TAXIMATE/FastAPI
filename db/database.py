from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from db.models import Base
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # replace this with your actual database URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()