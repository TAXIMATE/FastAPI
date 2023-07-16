from .teams import router as route_team
from .users import router as route_user

routers = [
    {"router": route_team, "prefix": "/teams", "tags": ["teams"]},
    {"router": route_user, "prefix": "/users", "tags": ["users"]},
]
