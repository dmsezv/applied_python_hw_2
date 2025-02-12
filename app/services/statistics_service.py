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

    def update_user_statistics(self, user_username: str, water: float, food: float, workout: float) -> UserStatistic:
        with get_session() as session:
            stmt = select(UserModel).where(UserModel.username == user_username)
            user = session.execute(stmt).scalar_one_or_none()
            if user:
                stmt = select(StatisticsModel).where(StatisticsModel.user_id == user.id)
                statistics = session.execute(stmt).scalar_one_or_none()
                if statistics:
                    statistics.water = water
                    statistics.food = food
                    statistics.workout = workout
                    statistics.updated_at = datetime.utcnow()
                    session.commit()
                    session.refresh(statistics)
                    return UserStatistic(**statistics.__dict__)
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
                    return UserStatistic(
                        water=statistics.water,
                        food=statistics.food,
                        workout=statistics.workout,
                        water_left=user.water_goal - statistics.water,
                        food_left=user.calories_goal - (statistics.food - statistics.workout),
                    ), user
                else:
                    return UserStatistic(
                        water=0,
                        food=0,
                        workout=0,
                        water_left=user.water_goal,
                        food_left=user.calories_goal
                    ), user
            return None, None
