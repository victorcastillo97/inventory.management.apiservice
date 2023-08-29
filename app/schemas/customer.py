from pydantic import BaseModel

class CustomerCreate(BaseModel):
    dni: int
    name: str

class Customer(CustomerCreate):
    id: int

    class Config:
        from_attributes = True