from sqlalchemy import Column, Integer, String, DateTime, Float
from database.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    weight = Column(Float)
    height = Column(Float)
    age = Column(Integer)
    activity = Column(Integer)
    city = Column(String)
    gender = Column(String)
    water_goal = Column(Float)
    calories_goal = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
