from sqlalchemy import Column, Integer, String
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    weight = Column(Integer)
    height = Column(Integer)
    age = Column(Integer)
    activity = Column(Integer)
    city = Column(String)
    calories = Column(Integer)
    gender = Column(String)

