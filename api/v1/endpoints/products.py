from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import SessionLocal
from services.products import get_products, create_product, get_product, delete_product
from schemas.product import ProductCreate
from fastapi.responses import JSONResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/{product_id}")
def read_product(product_id: int ,db: Session = Depends(get_db)):
    return get_product(db=db, product_id=product_id)

@router.post("/")
def create_products_router(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.delete("/{product_id}")
def delete_product_router(product_id: int, db: Session = Depends(get_db)):
    delete_product(db=db, product_id=product_id)
    return JSONResponse(content={"message": "Eliminado con éxito"}, status_code=status.HTTP_200_OK)