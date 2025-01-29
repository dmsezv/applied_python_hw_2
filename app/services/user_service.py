from sqlalchemy.orm import Session
from database.models import User
from sqlalchemy.exc import SQLAlchemyError
from database.db import SessionLocal


class UserService:
    def create_user(
        self, username: str, weight: int, height: int, age: int,
        activity: int, city: str, calories: int
    ) -> User:
        db: Session = SessionLocal()
        try:
            user = User(
                username=username,
                weight=weight,
                height=height,
                age=age,
                activity=activity,
                city=city,
                calories=calories
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Ошибка при сохранении пользователя: {e}")
            return None
        finally:
            db.close()
