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
    calories: float | None = None
    gender: str

    @field_validator("gender")
    def transform_gender(cls, v):
        return GENDER_MAN if v == "M" else GENDER_WOMAN

    @field_validator("calories")
    def transform_calories(cls, v):
        return "🤷‍♂️" if v is None else v
