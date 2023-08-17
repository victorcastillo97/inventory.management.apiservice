from core.database import Base, engine
from models import product, stock_product, customer, order 

Base.metadata.create_all(bind=engine)