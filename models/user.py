from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from core.database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255))
    password = Column(String(255))
