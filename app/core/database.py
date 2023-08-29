from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL

engine = create_engine(DATABASE_URL)

#Pool of sessions from ORM to SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#class model for tables
Base = declarative_base()