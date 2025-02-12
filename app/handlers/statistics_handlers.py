from services.statistics_service import StatisticsService
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    CHECK_PROGRESS, CHECK_PROGRESS_ERROR,
    FOOD_GET_TEXT, FOOD_FOUND_TEXT, FOOD_NOT_FOUND_TEXT, FOOD_ADD_TEXT, FOOD_NOT_ADDED_TEXT,
    STATISTICS_TEXT
)
from services.food_service import FoodService
from components.buttons import (
    YES_NO_INLINE_BUTTON, STATISTICS_MENU_BUTTONS
)
from datetime import date


FOOD_GET, FOOD_SET, FOOD_ADD = range(3)


async def start_statistics_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)
    await update.message.reply_text(STATISTICS_TEXT, reply_markup=keyboard)


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


async def get_food_handler(update: Update, context: CallbackContext):
    await update.message.reply_text(FOOD_GET_TEXT)
    return FOOD_SET


async def set_food_handler(update: Update, context: CallbackContext):
    food_service = FoodService()
    food = food_service.get_food_info(update.message.text)

    if food:
        keyboard = InlineKeyboardMarkup(YES_NO_INLINE_BUTTON)
        await update.message.reply_text(
            FOOD_FOUND_TEXT.format(
                product_name=food.title, calories_per_100g=food.calories),
            reply_markup=keyboard
        )
        context.user_data["food"] = food
        return FOOD_ADD
    else:
        await update.message.reply_text(FOOD_NOT_FOUND_TEXT)
        return FOOD_SET


async def add_food_handler(update: Update, context: CallbackContext):
    if update.callback_query.data == "yes":
        food = context.user_data["food"]
        statistics_service = StatisticsService()
        statistics_service.add_food(update.message.from_user.username, food)
        await update.message.reply_text(FOOD_ADD_TEXT)
        context.user_data.clear()
        return ConversationHandler.END
    else:
        await update.message.reply_text(FOOD_NOT_ADDED_TEXT)
        context.user_data.clear()
        return ConversationHandler.END
