from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

metadata_obj = MetaData()
url = "mysql+pymysql://root:123456@127.0.0.1:3306/botdb"
engine = create_engine(url)
session = sessionmaker(bind=engine)
