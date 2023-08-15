from fastapi import FastAPI
from api.v1.endpoints.users import router

app = FastAPI()

app.include_router(router)