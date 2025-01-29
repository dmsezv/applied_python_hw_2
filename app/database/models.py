from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.database.db import Base


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


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    weight = Column(Float)
    height = Column(Float)
    age = Column(Integer)
    activity = Column(String)
    city = Column(String)
    calories = Column(Integer)
