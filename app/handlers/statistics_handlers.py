from services.statistics_service import StatisticsService
from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    CHECK_PROGRESS, CHECK_PROGRESS_ERROR,
    FOOD_GET_TEXT, FOOD_FOUND_TEXT, FOOD_NOT_FOUND_TEXT, FOOD_ADD_TEXT, FOOD_NOT_ADDED_TEXT,
    FOOD_NOT_ADDED_ERROR_TEXT,
    FOOD_WEIGHT_TEXT, FOOD_ZERO_ERROR, FOOD_TYPE_ERROR,
    WORKOUT_NOT_ADDED_ERROR_TEXT,
    STATISTICS_TEXT,
    WORKOUT_GET_TEXT, WORKOUT_ADD_TEXT, WORKOUT_ZERO_ERROR, WORKOUT_TYPE_ERROR,
    RUN_BUTTON_LABEL, CYCLE_BUTTON_LABEL, SWIM_BUTTON_LABEL, PLANK_BUTTON_LABEL,
    GYM_BUTTON_LABEL, KLIMBING_BUTTON_LABEL, USER_NOT_FOUND_TEXT,
    WATER_GET_TEXT, WATER_ADD_TEXT, WATER_NOT_ADDED_ERROR_TEXT, WATER_ZERO_ERROR, WATER_TYPE_ERROR,
    WORKOUT_MINUTES_TEXT, BACK_BUTTON_LABEL,
    GRAPHICS_IN_PROGRESS_TEXT, GRAPHICS_ERROR_TEXT
)
from services.food_service import FoodService
from services.user_service import UserService
from components.buttons import (
    YES_NO_INLINE_BUTTON,
    CANCEL_BUTTON,
    STATISTICS_MENU_BUTTONS, WORKOUT_MENU_BUTTONS,
)
from services.goals_service import GoalsService
from services.graphics_generator_service import GraphicsGeneratorService
from states import (
    FOOD_SET, FOOD_ADD, FOOD_CALORIES_COUNT,
    WORKOUT_SET, WORKOUT_ADD,
    WATER_ADD
)
from datetime import date


async def start_statistics_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)
    await update.message.reply_text(STATISTICS_TEXT, reply_markup=keyboard)
    return ConversationHandler.END


async def get_daily_statistics_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    statistics_service = StatisticsService()
    statistics, user = statistics_service.get_daily_statistics(username)

    if statistics:
        food_left = user.calories_goal - (statistics.food + statistics.workout)
        water_left = user.water_goal - statistics.water
        await update.message.reply_text(
            CHECK_PROGRESS.format(
                date=date.today().strftime("%d.%m.%Y"),
                water=statistics.water,
                water_goal=user.water_goal,
                water_left=f"{water_left:.2f}",
                workout=f"{statistics.workout:.2f}",
                food=f"{statistics.food:.2f}",
                calories_goal=f"{user.calories_goal:.2f}",
                food_left=f"{food_left:.2f}"
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


async def get_workout_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(WORKOUT_MENU_BUTTONS)
    await update.message.reply_text(WORKOUT_GET_TEXT, reply_markup=keyboard)
    return WORKOUT_SET


async def set_workout_handler(update: Update, context: CallbackContext):
    keyboard_cancel = ReplyKeyboardMarkup(CANCEL_BUTTON)
    keyboard_statistics = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)
    workout_type = update.message.text
    # TODO: refactor this. bad code
    if workout_type == RUN_BUTTON_LABEL:
        context.user_data["workout_type"] = "run"
    elif workout_type == CYCLE_BUTTON_LABEL:
        context.user_data["workout_type"] = "cycle"
    elif workout_type == SWIM_BUTTON_LABEL:
        context.user_data["workout_type"] = "swim"
    elif workout_type == PLANK_BUTTON_LABEL:
        context.user_data["workout_type"] = "plank"
    elif workout_type == GYM_BUTTON_LABEL:
        context.user_data["workout_type"] = "gym"
    elif workout_type == KLIMBING_BUTTON_LABEL:
        context.user_data["workout_type"] = "klimbing"
    else:
        await update.message.reply_text(BACK_BUTTON_LABEL, reply_markup=keyboard_statistics)
        return ConversationHandler.END
    await update.message.reply_text(WORKOUT_MINUTES_TEXT, reply_markup=keyboard_cancel)
    return WORKOUT_ADD


async def add_workout_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)

    try:
        workout_minutes = float(update.message.text)
        if workout_minutes <= 0:
            await update.message.reply_text(WORKOUT_ZERO_ERROR)
            return WORKOUT_ADD
    except ValueError:
        await update.message.reply_text(WORKOUT_TYPE_ERROR)
        return WORKOUT_ADD

    user = UserService().get_user(update.message.from_user.username)
    if not user:
        await update.message.reply_text(USER_NOT_FOUND_TEXT, reply_markup=keyboard)
        return ConversationHandler.END

    goals_service = GoalsService()
    water_needed = goals_service.calculate_water_burned(
        user,
        context.user_data["workout_type"],
        workout_minutes
    )
    calories_burned = goals_service.calculate_calories_burned(
        user,
        context.user_data["workout_type"],
        workout_minutes
    )

    statistics_service = StatisticsService()
    if statistics_service.add_workout_to_statistics(
        update.message.from_user.username,
        calories_burned,
        water_needed
    ):
        await update.message.reply_text(
            WORKOUT_ADD_TEXT.format(
                water_needed=f"{water_needed:.2f}",
                calories_burned=f"{calories_burned:.2f}"
            ),
            reply_markup=keyboard
        )
    else:
        await update.message.reply_text(WORKOUT_NOT_ADDED_ERROR_TEXT, reply_markup=keyboard)
    context.user_data.clear()
    return ConversationHandler.END


async def set_water_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(CANCEL_BUTTON)
    await update.message.reply_text(WATER_GET_TEXT, reply_markup=keyboard)
    return WATER_ADD


async def add_water_handler(update: Update, context: CallbackContext):
    keyboard = ReplyKeyboardMarkup(STATISTICS_MENU_BUTTONS)

    try:
        water_amount = float(update.message.text)
        if water_amount <= 0:
            await update.message.reply_text(WATER_ZERO_ERROR)
            return WATER_ADD
    except ValueError:
        await update.message.reply_text(WATER_TYPE_ERROR)
        return WATER_ADD

    statistics_service = StatisticsService()
    if statistics_service.add_water_to_statistics(
        update.message.from_user.username,
        water_amount
    ):
        await update.message.reply_text(WATER_ADD_TEXT.format(water_needed=water_amount), reply_markup=keyboard)
    else:
        await update.message.reply_text(WATER_NOT_ADDED_ERROR_TEXT, reply_markup=keyboard)
    context.user_data.clear()
    return ConversationHandler.END


async def get_graphics_handler(update: Update, context: CallbackContext):
    await update.message.reply_text(GRAPHICS_IN_PROGRESS_TEXT)

    username = update.message.from_user.username
    graphics_generator_service = GraphicsGeneratorService()
    chart = graphics_generator_service.generate_weekly_charts(username)
    if not chart:
        await update.message.reply_text(GRAPHICS_ERROR_TEXT)
        return ConversationHandler.END
    await update.message.reply_photo(photo=chart)
    context.user_data.clear()
    return ConversationHandler.END
