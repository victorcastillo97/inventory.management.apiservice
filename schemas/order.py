from pydantic import BaseModel
from datetime import datetime

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