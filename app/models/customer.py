from sqlalchemy import Column, Integer, String
from core.database import Base
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer, index=True)
    name = Column(String(255))

    orders = relationship('Order', back_populates='customer')
