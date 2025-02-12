from telegram import Update, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    HELLO_TEXT,
    WEIGHT_TEXT, WEIGHT_TEXT_SAVED, WEIGHT_TYPE_ERROR, WEIGHT_ZERO_ERROR,
    HEIGHT_TEXT_SAVED, HEIGHT_TYPE_ERROR, HEIGHT_ZERO_ERROR,
    AGE_TEXT_SAVED, AGE_TYPE_ERROR, AGE_ZERO_ERROR,
    ACTIVITY_TEXT_SAVED, ACTIVITY_TYPE_ERROR, ACTIVITY_ZERO_ERROR,
    CITY_TEXT_SAVED, CITY_TYPE_ERROR,
    PROFILE_UPDATED, PROFILE_ERROR, PROFILE_SAVING_IN_PROGRESS,
    GENDER_TEXT_SAVED, GENDER_TYPE_ERROR, GENDER_MAN, GENDER_WOMAN, 
    CITY_ERROR, CITY_WEATHER_IN_PROGRESS
)
from components.buttons import MAN_WOMAN_INLINE_BUTTONS, MAIN_MENU_BUTTONS
from services.user_service import UserService
from services.goals_service import GoalsService
from services.weather_service import WeatherService


WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, GENDER = range(6)


async def set_profile_start(update: Update, context: CallbackContext) -> int:
    username = update.message.from_user.username
    context.user_data["username"] = username
    message = f"{HELLO_TEXT.format(username=username)}\n\n{WEIGHT_TEXT}"
    await update.message.reply_text(message)
    context.user_data["current_state"] = WEIGHT
    return WEIGHT


async def weight_handler(update: Update, context: CallbackContext) -> int:
    try:
        weight = float(update.message.text)
        if weight <= 0:
            await update.message.reply_text(WEIGHT_ZERO_ERROR)
            return WEIGHT
    except ValueError:
        await update.message.reply_text(WEIGHT_TYPE_ERROR)
        return WEIGHT

    context.user_data["weight"] = update.message.text
    await update.message.reply_text(WEIGHT_TEXT_SAVED.format(weight=update.message.text))
    context.user_data["current_state"] = HEIGHT
    return HEIGHT


async def height_handler(update: Update, context: CallbackContext) -> int:
    try:
        height = float(update.message.text)
        if height <= 0:
            await update.message.reply_text(HEIGHT_ZERO_ERROR)
            return HEIGHT
    except ValueError:
        await update.message.reply_text(HEIGHT_TYPE_ERROR)
        return HEIGHT

    context.user_data["height"] = update.message.text
    await update.message.reply_text(HEIGHT_TEXT_SAVED.format(height=update.message.text))
    context.user_data["current_state"] = AGE
    return AGE


async def age_handler(update: Update, context: CallbackContext) -> int:
    try:
        age = float(update.message.text)
        if age <= 0:
            await update.message.reply_text(AGE_ZERO_ERROR)
            return AGE
    except ValueError:
        await update.message.reply_text(AGE_TYPE_ERROR)
        return AGE

    context.user_data["age"] = update.message.text
    await update.message.reply_text(AGE_TEXT_SAVED.format(age=update.message.text))
    context.user_data["current_state"] = ACTIVITY
    return ACTIVITY


async def activity_handler(update: Update, context: CallbackContext) -> int:
    try:
        activity = float(update.message.text)
        if activity <= 0:
            await update.message.reply_text(ACTIVITY_ZERO_ERROR)
            return ACTIVITY
    except ValueError:
        await update.message.reply_text(ACTIVITY_TYPE_ERROR)
        return ACTIVITY

    context.user_data["activity"] = update.message.text
    await update.message.reply_text(ACTIVITY_TEXT_SAVED.format(activity=update.message.text))
    context.user_data["current_state"] = CITY
    return CITY


async def city_handler(update: Update, context: CallbackContext) -> int:
    try:
        city = update.message.text
        if not city:
            await update.message.reply_text(CITY_TYPE_ERROR)
            return CITY
    except ValueError:
        await update.message.reply_text(CITY_TYPE_ERROR)
        return CITY

    await update.message.reply_text(CITY_WEATHER_IN_PROGRESS.format(city=city))
    weather_service = WeatherService()
    temperature = await weather_service.get_weather(city)

    if temperature is None:
        await update.message.reply_text(CITY_ERROR)
        return CITY

    context.user_data["city"] = update.message.text
    context.user_data["temperature"] = temperature
    reply_markup = InlineKeyboardMarkup(MAN_WOMAN_INLINE_BUTTONS)
    await update.message.reply_text(
        CITY_TEXT_SAVED.format(
            city=update.message.text,
            temperature=temperature
        ),
        reply_markup=reply_markup
    )
    context.user_data["current_state"] = GENDER
    return GENDER


async def gender_handler(update: Update, context: CallbackContext) -> int:
    if update.callback_query:
        query = update.callback_query
        await query.answer()

        if query.data == "M":
            context.user_data["gender"] = "M"
        elif query.data == "F":
            context.user_data["gender"] = "F"
        else:
            reply_markup = InlineKeyboardMarkup(MAN_WOMAN_INLINE_BUTTONS)
            await query.message.reply_text(GENDER_TYPE_ERROR, reply_markup=reply_markup)
            return GENDER

        await query.message.reply_text(
            GENDER_TEXT_SAVED.format(
                gender=GENDER_MAN if query.data == "M" else GENDER_WOMAN
            )
        )

        await query.message.reply_text(PROFILE_SAVING_IN_PROGRESS)

        user = update_user_profile(update, context)

        if user is None:
            await query.message.reply_text(PROFILE_ERROR)
            return GENDER

        reply_markup = ReplyKeyboardMarkup(MAIN_MENU_BUTTONS, one_time_keyboard=True)
        await query.message.reply_text(PROFILE_UPDATED.format(
            temperature=context.user_data["temperature"],
            city=context.user_data["city"],
            calories_goal=user.calories_goal,
            water_goal=user.water_goal
        ), reply_markup=reply_markup)
        context.user_data.clear()
        return ConversationHandler.END
    else:
        reply_markup = InlineKeyboardMarkup(MAN_WOMAN_INLINE_BUTTONS)
        await update.message.reply_text(GENDER_TYPE_ERROR, reply_markup=reply_markup)
        return GENDER


def update_user_profile(update: Update, context: CallbackContext) -> int:
    goals_service = GoalsService()
    water_goal = goals_service.calculate_water_goal(
        weight=float(context.user_data["weight"]),
        activity_minutes=int(context.user_data["activity"]),
        temperature=float(context.user_data["temperature"])
    )
    calories_goal = goals_service.calculate_calories_goal(
        weight=float(context.user_data["weight"]),
        height=float(context.user_data["height"]),
        age=int(context.user_data["age"]),
        activity_level=int(context.user_data["activity"])
    )

    return UserService().update_user(
        username=context.user_data["username"],
        weight=context.user_data["weight"],
        height=context.user_data["height"],
        age=context.user_data["age"],
        activity=context.user_data["activity"],
        city=context.user_data["city"],
        gender=context.user_data["gender"],
        water_goal=water_goal,
        calories_goal=calories_goal
    )
