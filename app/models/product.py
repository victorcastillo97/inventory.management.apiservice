from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base
from models.stock_product import Stock_Product
from models.order import Order

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    brand = Column(String(255))
    description = Column(String(255))
    price = Column(Integer)
    stock = Column(Integer)

    stock_product = relationship('Stock_Product', back_populates='product')
    orders = relationship('Order', back_populates='product')