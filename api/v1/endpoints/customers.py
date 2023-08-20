from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from services.customers import get_customers, create_customer
from schemas.customer import CustomerCreate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/{customer_id}")
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return get_customers(db=db, customer_id=customer_id)

@router.post("/")
def create_customer_router(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)