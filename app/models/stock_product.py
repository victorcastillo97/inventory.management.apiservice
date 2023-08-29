from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from core.database import Base

class Stock_Product(Base):
    __tablename__ = "stock_products"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    stock = Column(Integer)

    product = relationship('Product', back_populates='stock_product')