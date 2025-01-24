from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    name: str


class UserProfile(BaseModel):
    weight: float
    height: float
    age: int
    activity: int
    city: str
    calories: float
