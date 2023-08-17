from pydantic import BaseModel

class StockProductCreate(BaseModel):
    product_id: int
    stock: int

class StockProduct(StockProductCreate):
    id: int

    class Config:
        from_attributes = True