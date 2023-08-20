from fastapi import FastAPI
from api.v1.endpoints import products, stock_products, customers, orders

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(stock_products.router, prefix="/stock_products", tags=["stock_products"])
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])