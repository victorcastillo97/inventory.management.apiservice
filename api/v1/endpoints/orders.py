from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from schemas.order import OrderCreate, OrderCompleteCreate
from services.orders import get_orders, create_order, create_complete_order

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_orders(db: Session = Depends(get_db)):
    return get_orders(db=db)

@router.post("")
def create_order_router(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order=order)

@router.post("/complete")
def create_complete_order_router(order: OrderCompleteCreate, db: Session = Depends(get_db)):
    return create_complete_order(db=db, order=order)