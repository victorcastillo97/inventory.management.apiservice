from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:password@localhost:33060/storedb")

meta = MetaData()

conn = engine.connect()

