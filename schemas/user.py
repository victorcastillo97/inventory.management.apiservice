from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class User(UserCreate):
    id: int

    class Config:
        from_attributes = True