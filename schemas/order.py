from pydantic import BaseModel
from datetime import datetime

class OrderCompleteCreate(BaseModel):
    dni: int
    name: str
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    product_id: int
    customer_id: int
    order_date: datetime
    quantity: int
    price_unit: int

class Order(OrderCreate):
    id: int

    class Config:
        from_attributes = True