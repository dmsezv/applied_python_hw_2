from database.db import get_session
from database.models import User as UserModel
from schemas.models import User
from sqlalchemy import select
from datetime import datetime


class UserService:
    def update_user(
        self, username: str, weight: int, height: int, age: int,
        activity: int, city: str, gender: str,
        water_goal: int, calories_goal: int, temperature: float
    ) -> User:
        with get_session() as session:
            try:
                user = session.query(UserModel).filter(UserModel.username == username).first()
                if user:
                    user.weight = weight
                    user.height = height
                    user.age = age
                    user.activity = activity
                    user.city = city
                    user.gender = gender
                    user.water_goal = water_goal
                    user.calories_goal = calories_goal
                    user.temperature = temperature
                    user.updated_at = datetime.utcnow()
                else:
                    user = UserModel(
                        username=username,
                        weight=weight,
                        height=height,
                        age=age,
                        activity=activity,
                        city=city,
                        gender=gender,
                        water_goal=water_goal,
                        calories_goal=calories_goal,
                        temperature=temperature,
                        created_at=datetime.utcnow(),
                        updated_at=datetime.utcnow()
                    )
                    session.add(user)
                session.commit()
                session.refresh(user)
                return User(**user.__dict__)
            except Exception as e:
                print(f"Ошибка при сохранении пользователя: {e}")
                return None

    def get_user(self, username: str) -> User:
        with get_session() as session:
            try:
                stmt = select(UserModel).where(UserModel.username == username)
                result = session.execute(stmt).scalar()
                if result:
                    return User(**result.__dict__)
                return None
            except Exception as e:
                print(f"Ошибка при получении пользователя: {e}")
                return None

    def delete_user(self, username: str) -> bool:
        with get_session() as session:
            try:
                user = session.query(UserModel).filter(UserModel.username == username).first()
                if user:
                    session.delete(user)
                    session.commit()
                    return True
                return False
            except Exception as e:
                print(f"Ошибка при удалении пользователя: {e}")
                return False
