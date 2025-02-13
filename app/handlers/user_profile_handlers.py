from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from services.user_service import UserService
from services.weather_service import WeatherService
from services.goals_service import GoalsService
from strings import (
    PROFILE_NOT_FOUND, PROFILE_VIEW, PROFILE_DELETED, PROFILE_DELETE_ERROR, 
    CITY_WEATHER_IN_PROGRESS, CITY_ERROR, CITY_WEATHER_SUCCESS,
    UPDATE_GOALS_TEXT, UPDATE_GOALS_SUCCESS, UPDATE_GOALS_ERROR
)

SHOW_PROFILE, DELETE_PROFILE = range(2)


async def view_profile_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    user = UserService().get_user(username)

    if user:
        await update.message.reply_text(
            PROFILE_VIEW.format(
                weight=user.weight,
                height=user.height,
                age=user.age,
                activity=user.activity,
                city=user.city,
                gender=user.gender,
                water_goal=user.water_goal,
                calories_goal=user.calories_goal
            )
        )
    else:
        await update.message.reply_text(PROFILE_NOT_FOUND)

    return ConversationHandler.END


async def delete_profile_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    result_ok = UserService().delete_user(username)

    if result_ok:
        await update.message.reply_text(PROFILE_DELETED)
    else:
        await update.message.reply_text(PROFILE_DELETE_ERROR)

    return ConversationHandler.END


async def update_goals_handler(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    user = UserService().get_user(username)

    if user is None:
        await update.message.reply_text(PROFILE_NOT_FOUND)
        return ConversationHandler.END

    await update.message.reply_text(CITY_WEATHER_IN_PROGRESS.format(city=user.city))

    weather_service = WeatherService()
    temperature = await weather_service.get_weather(user.city)

    if temperature is None:
        await update.message.reply_text(CITY_ERROR)
    else:
        await update.message.reply_text(CITY_WEATHER_SUCCESS.format(city=user.city, temperature=temperature))
        await update.message.reply_text(UPDATE_GOALS_TEXT)
        goals_service = GoalsService()
        water_goal = goals_service.calculate_water_goal(
            weight=user.weight,
            activity_minutes=user.activity,
            temperature=temperature
        )
        calories_goal = goals_service.calculate_calories_goal(
            weight=user.weight,
            height=user.height,
            age=user.age,
            activity_level=user.activity,
            gender=user.gender
        )

        user = UserService().update_user(
            username=username,
            weight=user.weight,
            height=user.height,
            age=user.age,
            activity=user.activity,
            city=user.city,
            gender=user.gender,
            water_goal=water_goal,
            calories_goal=calories_goal,
            temperature=temperature
        )

        if user is None:
            await update.message.reply_text(UPDATE_GOALS_ERROR)
        else:
            await update.message.reply_text(UPDATE_GOALS_SUCCESS.format(
                water_goal=water_goal,
                calories_goal=calories_goal
            ))

    return ConversationHandler.END
