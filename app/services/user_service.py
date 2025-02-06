# from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database.db import get_db
from database.models import User


class UserService:
    def create_user(
        self, username: str, weight: int, height: int, age: int,
        activity: int, city: str, calories: int, gender: str
    ) -> User:
        with get_db() as db:
            try:
                user = User(
                    username=username,
                    weight=weight,
                    height=height,
                    age=age,
                    activity=activity,
                    city=city,
                    calories=calories,
                    gender=gender
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
            except SQLAlchemyError as e:
                print(f"Ошибка при сохранении пользователя: {e}")
                return None

    def update_user(self, user: User, **kwargs) -> User:
        with get_db() as db:
            for key, value in kwargs.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
            return user or None

    def get_user(self, username: str) -> User:
        with get_db() as db:
            return db.query(User).filter(User.username == username).first()
