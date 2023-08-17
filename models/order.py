from sqlalchemy import ForeignKey, Column, Integer, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
from models.customer import Customer
import datetime

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    quantity = Column(Integer)
    price_unit = Column(Integer)

    product = relationship('Product', back_populates='orders')
    customer = relationship('Customer', back_populates='orders')