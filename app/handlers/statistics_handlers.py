from services.statistics_service import StatisticsService
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    CHECK_PROGRESS, CHECK_PROGRESS_ERROR,
    FOOD_GET_TEXT, FOOD_FOUND_TEXT, FOOD_NOT_FOUND_TEXT, FOOD_ADD_TEXT, FOOD_NOT_ADDED_TEXT,
    FOOD_NOT_ADDED_ERROR_TEXT,
    FOOD_WEIGHT_TEXT, FOOD_ZERO_ERROR, FOOD_TYPE_ERROR,
    STATISTICS_TEXT
)
from services.food_service import FoodService
from components.buttons import (
    YES_NO_INLINE_BUTTON, STATISTICS_MENU_BUTTONS, CANCEL_BUTTON
)
from datetime import date


FOOD_GET, FOOD_SET, FOOD_ADD, FOOD_CALORIES_COUNT = range(4)


async def start_statistics_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)
    await update.message.reply_text(STATISTICS_TEXT, reply_markup=keyboard)
    return ConversationHandler.END


async def get_daily_statistics_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    statistics_service = StatisticsService()
    statistics, user = statistics_service.get_daily_statistics(username)

    if statistics:
        await update.message.reply_text(
            CHECK_PROGRESS.format(
                date=date.today().strftime("%d.%m.%Y"),
                water=statistics.water,
                water_goal=user.water_goal,
                water_left=statistics.water_left,
                workout=statistics.workout,
                food=statistics.food,
                calories_goal=user.calories_goal,
                food_left=statistics.food_left
            )
        )
    else:
        await update.message.reply_text(CHECK_PROGRESS_ERROR)

    return ConversationHandler.END


async def get_food_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(CANCEL_BUTTON)
    await update.message.reply_text(FOOD_GET_TEXT, reply_markup=keyboard)
    return FOOD_SET


async def set_food_handler(update: Update, context: CallbackContext):
    food_service = FoodService()
    food = await food_service.get_food_info(update.message.text)

    if food:
        keyboard = InlineKeyboardMarkup(YES_NO_INLINE_BUTTON)
        await update.message.reply_text(
            FOOD_FOUND_TEXT.format(
                product_name=food.title,
                calories_per_100g=food.calories
            ),
            reply_markup=keyboard
        )
        context.user_data["food"] = food
        return FOOD_ADD
    else:
        await update.message.reply_text(FOOD_NOT_FOUND_TEXT)
        return FOOD_SET


async def add_food_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)

    if update.callback_query.data == "yes":
        await update.callback_query.message.reply_text(FOOD_WEIGHT_TEXT)
        return FOOD_CALORIES_COUNT
    else:
        await update.callback_query.message.reply_text(FOOD_NOT_ADDED_TEXT, reply_markup=keyboard)
        context.user_data.clear()
        return ConversationHandler.END


async def get_calories_count_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)

    try:
        calories_count = float(update.message.text)
        if calories_count <= 0:
            await update.message.reply_text(FOOD_ZERO_ERROR)
            return FOOD_CALORIES_COUNT
    except ValueError:
        await update.message.reply_text(FOOD_TYPE_ERROR)
        return FOOD_CALORIES_COUNT

    calories_count = context.user_data["food"].calories / 100 * calories_count

    statistics_service = StatisticsService()
    if statistics_service.add_food_to_statistics(
        update.message.from_user.username,
        calories_count
    ):
        await update.message.reply_text(FOOD_ADD_TEXT, reply_markup=keyboard)
    else:
        await update.message.reply_text(FOOD_NOT_ADDED_ERROR_TEXT, reply_markup=keyboard)
    context.user_data.clear()
    return ConversationHandler.END


async def get_water_handler(update: Update, context: CallbackContext):
    pass


async def get_workout_handler(update: Update, context: CallbackContext):
    pass
