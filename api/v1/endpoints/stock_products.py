from fastapi import APIRouter, Depends, status
from core.database import SessionLocal
from sqlalchemy.orm import Session
from services.stock_products import get_stock_product, create_stock_product, update_stock_product,delete_stock_product
from schemas.stock_product import StockProductCreate
from fastapi.responses import JSONResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{stock_product_id}")
def read_stock_product(stock_product_id: int, db: Session = Depends(get_db)):
    return get_stock_product(db=db, stock_product_id=stock_product_id)

@router.post("/")
def create_stock_product_router(stock_product: StockProductCreate, db: Session = Depends(get_db)):
    return create_stock_product(db=db, stock_product=stock_product)

@router.put("/")
def update_stock_product_router(stock_product: StockProductCreate, db: Session = Depends(get_db)):
    return update_stock_product(db=db, stock_product=stock_product)

@router.delete("/{product_id}")
def delete_stock_product_router(product_id:int, db: Session = Depends(get_db)):
    delete_stock_product(db=db, product_id=product_id)
    return JSONResponse(content={"message": "Eliminado con éxito"}, status_code=status.HTTP_200_OK)