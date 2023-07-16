from fastapi import FastAPI
from api.endpoints import routers

app = FastAPI()

for route_info in routers:
    app.include_router(route_info["router"], prefix=route_info["prefix"], tags=route_info["tags"])
