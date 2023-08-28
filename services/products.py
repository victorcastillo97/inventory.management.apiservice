from sqlalchemy.orm import Session
from models.product import Product
from schemas.product import ProductCreate, Product as SchemaProduct

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_stock_product(stock_product_update: int, product: Product,  db: Session):
    setattr(product, "stock", stock_product_update)
    db.commit()
    db.refresh(product)
    return product

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_update: SchemaProduct):
    print("product: ")
    print(product_update.dict())
    db_product = db.query(Product).filter(Product.id == product_update.dict()["id"]).first()

    if not db_product:
        return None

    for key, value in product_update.dict().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    db.delete(db_product)
    db.commit()