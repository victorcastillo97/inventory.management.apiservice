from fastapi import APIRouter, Depends, HTTPException
from core.database import SessionLocal
from services.users import get_users, get_user, create_user
from sqlalchemy.orm import Session
from schemas.user import User, UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_user

@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)