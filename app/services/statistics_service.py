from database.db import get_session
from database.models import User as UserModel, Statistics as StatisticsModel
from schemas.models import UserStatistic, User
from sqlalchemy import select
from datetime import datetime, date


class StatisticsService:
    def get_user_statistics(self, user_username: str) -> UserStatistic:
        with get_session() as session:
            stmt = select(UserModel).where(UserModel.username == user_username) 
            user = session.execute(stmt).scalar_one_or_none()
            if user:
                stmt = select(StatisticsModel).where(StatisticsModel.user_id == user.id)
                return session.execute(stmt).scalar_one_or_none()
            return None

    def get_daily_statistics(self, user_username: str) -> (UserStatistic, User):
        with get_session() as session:
            stmt = select(UserModel).where(UserModel.username == user_username)
            user = session.execute(stmt).scalar_one_or_none()
            if user:
                today_start = datetime.combine(date.today(), datetime.min.time())
                today_end = datetime.combine(date.today(), datetime.max.time())
                stmt = select(StatisticsModel).where(
                    StatisticsModel.user_id == user.id,
                    StatisticsModel.created_at >= today_start,
                    StatisticsModel.created_at <= today_end
                )
                statistics = session.execute(stmt).scalar_one_or_none()
                if statistics:
                    water_left = user.water_goal - statistics.water
                    calories_left = user.calories_goal - (statistics.food - statistics.workout)
                    return UserStatistic(
                        user_id=user.id,
                        water=statistics.water,
                        food=statistics.food,
                        workout=statistics.workout,
                        water_left=water_left,
                        food_left=calories_left
                    ), User(**user.__dict__)
                else:
                    return UserStatistic(
                        user_id=0,
                        water=0,
                        food=0,
                        workout=0,
                        water_left=user.water_goal,
                        food_left=user.calories_goal
                    ), User(**user.__dict__)
            return None, None

    def add_food_to_statistics(self, username, calories):
        with get_session() as session:
            try:
                user = session.execute(select(UserModel).where(UserModel.username == username)).scalar_one()
                if not user:
                    return False
                today_start = datetime.combine(date.today(), datetime.min.time())
                today_end = datetime.combine(date.today(), datetime.max.time())
                stmt = select(StatisticsModel).where(
                    StatisticsModel.user_id == user.id,
                    StatisticsModel.created_at >= today_start,
                    StatisticsModel.created_at <= today_end
                )
                statistics = session.execute(stmt).scalar_one_or_none()
                if statistics:
                    statistics.food += calories
                    session.commit()
                else:
                    statistics = StatisticsModel(
                        user_id=user.id,
                        food=calories,
                        water=0,
                        workout=0,
                        updated_at=datetime.now(),
                        created_at=datetime.now()
                    )
                    session.add(statistics)
                    session.commit()
                    session.refresh(statistics)
                return True
            except Exception as e:
                print(f"Ошибка при добавлении продукта в статистику: {e}")
                return False

    def add_workout_to_statistics(self, username, calories_burned, water_burned):
        with get_session() as session:
            try:
                user = session.execute(select(UserModel).where(UserModel.username == username)).scalar_one()
                if not user:
                    return False
                today_start = datetime.combine(date.today(), datetime.min.time())
                today_end = datetime.combine(date.today(), datetime.max.time())
                stmt = select(StatisticsModel).where(
                    StatisticsModel.user_id == user.id,
                    StatisticsModel.created_at >= today_start,
                    StatisticsModel.created_at <= today_end
                )
                statistics = session.execute(stmt).scalar_one_or_none()
                if statistics:
                    statistics.workout += calories_burned
                    statistics.water -= water_burned
                    session.commit()
                else:
                    statistics = StatisticsModel(
                        user_id=user.id,
                        food=0,
                        water=-water_burned,
                        workout=calories_burned,
                        updated_at=datetime.now(),
                        created_at=datetime.now()
                    )
                    session.add(statistics)
                    session.commit()
                    session.refresh(statistics)
                return True
            except Exception as e:
                print(f"Ошибка при добавлении тренировки в статистику: {e}")
                return False

    def add_water_to_statistics(self, username, water_amount):
        with get_session() as session:
            try:
                user = session.execute(select(UserModel).where(UserModel.username == username)).scalar_one()
                if not user:
                    return False
                today_start = datetime.combine(date.today(), datetime.min.time())
                today_end = datetime.combine(date.today(), datetime.max.time())
                stmt = select(StatisticsModel).where(
                    StatisticsModel.user_id == user.id,
                    StatisticsModel.created_at >= today_start,
                    StatisticsModel.created_at <= today_end
                )
                statistics = session.execute(stmt).scalar_one_or_none()
                if statistics:
                    statistics.water += water_amount
                    session.commit()
                else:
                    statistics = StatisticsModel(
                        user_id=user.id,
                        food=0,
                        water=water_amount,
                        workout=0,
                        updated_at=datetime.now(),
                        created_at=datetime.now()
                    )
                    session.add(statistics)
                    session.commit()
                    session.refresh(statistics)
                return True
            except Exception as e:
                print(f"Ошибка при добавлении тренировки в статистику: {e}")
                return False