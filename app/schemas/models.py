from pydantic import BaseModel, field_validator
from strings import GENDER_MAN, GENDER_WOMAN


class BaseSchema(BaseModel):
    class Config:
        orm_mode = True


class User(BaseSchema):
    username: str
    weight: float
    height: float
    age: int
    activity: int
    city: str
    gender: str
    water_goal: float
    calories_goal: float

    @field_validator("gender")
    def transform_gender(cls, v):
        return GENDER_MAN if v == "M" else GENDER_WOMAN


class UserStatistic(BaseSchema):
    user_id: int
    water: float
    food: float
    workout: float
    water_left: float
    food_left: float


class Food(BaseSchema):
    request: str
    title: str
    calories: float
