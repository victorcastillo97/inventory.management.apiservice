from core.database import Base, engine
from models import user

Base.metadata.create_all(bind=engine)