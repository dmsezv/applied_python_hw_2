import matplotlib.pyplot as plt
import io
from services.statistics_service import StatisticsService
from services.user_service import UserService
from strings import (
    WATER_GRAPHICS_TEXT,
    CALORIES_GRAPHICS_TEXT,
    WATER_GRAPHICS_TEXT_Y_AXIS,
    CALORIES_GRAPHICS_TEXT_Y_AXIS,
    DATE_TEXT,
    WATER_GRAPHICS_GOAL_TEXT,
    CALORIES_GRAPHICS_GOAL_TEXT
)


class GraphicsGeneratorService:
    def generate_weekly_charts(self, username):
        statistics = StatisticsService().get_weekly_statistics(username)

        dates = [stat.created_at.strftime("%d-%m-%Y") for stat in statistics]
        water = [stat.water for stat in statistics]
        food = [stat.food for stat in statistics]

        user = UserService().get_user(username)
        water_goal = user.water_goal
        calories_goal = user.calories_goal

        plt.figure(figsize=(10, 5))

        plt.subplot(2, 1, 1)
        plt.plot(dates, water, label=WATER_GRAPHICS_TEXT_Y_AXIS, color="blue")
        plt.axhline(y=water_goal, color="green", linestyle="--", label=WATER_GRAPHICS_GOAL_TEXT)
        plt.title(WATER_GRAPHICS_TEXT)
        plt.xlabel(DATE_TEXT)
        plt.ylabel(WATER_GRAPHICS_TEXT_Y_AXIS)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        plt.subplot(2, 1, 2)
        plt.plot(dates, food, label=CALORIES_GRAPHICS_TEXT_Y_AXIS, color="red")
        plt.axhline(y=calories_goal, color="green", linestyle="--", label=CALORIES_GRAPHICS_GOAL_TEXT)
        plt.title(CALORIES_GRAPHICS_TEXT)
        plt.xlabel(DATE_TEXT)
        plt.ylabel(CALORIES_GRAPHICS_TEXT_Y_AXIS)
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close()

        return buf
