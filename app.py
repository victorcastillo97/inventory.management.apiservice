from fastapi import FastAPI
from api.v1.endpoints import users, products

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"])