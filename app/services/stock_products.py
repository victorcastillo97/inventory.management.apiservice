from sqlalchemy.orm import Session
from models.stock_product import Stock_Product
from schemas.stock_product import StockProductCreate

def create_stock_product(stock_product: StockProductCreate, db=Session):
    db_stock_product = Stock_Product(**stock_product.dict())
    db.add(db_stock_product)
    db.commit()
    db.refresh(db_stock_product)
    return db_stock_product

def get_stock_product(stock_product_id: int, db = Session):
    return db.query(Stock_Product).filter(Stock_Product.id == stock_product_id).first()

def update_stock_product(stock_product: StockProductCreate, db: Session):
    result = db.query(Stock_Product).filter(Stock_Product.product_id == stock_product.product_id).update(stock_product.dict())
    db.commit()
    return result

def delete_stock_product(db: Session, product_id: int):
    db_product = db.query(Stock_Product).filter(Stock_Product.product_id == product_id).first()
    db.delete(db_product)
    db.commit()