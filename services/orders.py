from sqlalchemy.orm import Session
from models.order import Order 
from schemas.order import OrderCreate

def get_orders(db:Session):
    return db.query(Order).all()

def create_order(db:Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order