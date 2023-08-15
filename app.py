from fastapi import FastAPI
from api.v1.endpoints import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])