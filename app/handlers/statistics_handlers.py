from services.statistics_service import StatisticsService
from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from strings import CHECK_PROGRESS, CHECK_PROGRESS_ERROR
from services.food_service import FoodService
from datetime import date


async def get_daily_statistics_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    statistics_service = StatisticsService()
    statistics, user = statistics_service.calculate_daily_statistics(username)

    if statistics:
        update.message.reply_text(
            CHECK_PROGRESS.format(
                date=date.today().strftime("%d.%m.%Y"),
                water=statistics.water,
                water_goal=user.water_goal,
                water_left=statistics.water_left,
                food=statistics.food,
                calories_goal=user.calories_goal,
                food_left=statistics.food_left
            )
        )
    else:
        update.message.reply_text(CHECK_PROGRESS_ERROR)

    return ConversationHandler.END


async def set_food_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    food_service = FoodService()
    food = food_service.get_food(username)

    if food:
        update.message.reply_text(FOOD_SET)
    else:
        update.message.reply_text(FOOD_NOT_FOUND)

    return ConversationHandler.END
