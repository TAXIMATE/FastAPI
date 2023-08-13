from models import Base
from db_session import engine, get_db

Base.metadata.create_all(bind=engine)
