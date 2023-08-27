from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    brand: str
    description: str
    price: int
    stock: int

class Product(ProductCreate):
    id: int

    class Config:
        from_attributes = True