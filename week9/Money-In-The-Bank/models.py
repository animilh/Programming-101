from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from settings import DB_CONNECTION_STRING

Base = declarative_base()

class Client(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    balance = Column(Float)
    message = Column(String)
	
    def __str__(self):
        return "{} - {}".format(self.id, self.username)

    def __repr__(self):
        return self.__str__()

engine = create_engine(DB_CONNECTION_STRING)

Base.metadata.create_all(engine)
