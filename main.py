from fastapi import FastAPI
from api.endpoints import endpoint1

app = FastAPI()

app.include_router(endpoint1.router)
