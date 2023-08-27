from sqlalchemy.orm import Session
from models.order import Order 
from schemas.order import OrderCreate, OrderCompleteCreate
from schemas.customer import CustomerCreate
from services.customers import get_customer_by_dni, create_customer
from services.products import get_product

def get_orders(db:Session):
    return db.query(Order).all()

def create_order(db:Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_complete_order(db: Session, order:OrderCompleteCreate):
    customer = get_customer_by_dni(db, order.dni)

    if not customer:
        customer_data = CustomerCreate(dni=order.dni, name=order.name)
        customer = create_customer(db, customer_data)

    product = get_product(db, order.product_id)

    product_id: int
    customer_id: int
    order_date: datetime
    quantity: int
    price_unit: int

    db_order = Order(
        customer_id = customer.id,
        product_id = order.product_id,
        price_unit = product.price,
        quantity = order.quantity
    )
    
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
