from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    WEIGHT_TEXT, HEIGHT_TEXT, AGE_TEXT, ACTIVITY_TEXT,
    CITY_TEXT, CALORIES_TEXT, PROFILE_UPDATED, PROFILE_ERROR
)
# from sqlalchemy.orm import Session
# from database.db import SessionLocal
from services.user_service import UserService

WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES, OTHER = range(7)


async def set_profile_start(update: Update, context: CallbackContext) -> int:
    username = update.message.from_user.username
    context.user_data["username"] = username
    await update.message.reply_text(f"Привет, {username}! {WEIGHT_TEXT}")
    context.user_data["current_state"] = WEIGHT
    return WEIGHT


async def weight_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await set_profile_start(update, context)
    context.user_data["weight"] = update.message.text
    await update.message.reply_text(HEIGHT_TEXT)
    context.user_data["current_state"] = HEIGHT
    return HEIGHT


async def height_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await weight_handler(update, context)
    context.user_data["height"] = update.message.text
    await update.message.reply_text(AGE_TEXT)
    context.user_data["current_state"] = AGE
    return AGE


async def age_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await height_handler(update, context)
    context.user_data["age"] = update.message.text
    await update.message.reply_text(ACTIVITY_TEXT)
    context.user_data["current_state"] = ACTIVITY
    return ACTIVITY


async def activity_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await age_handler(update, context)
    context.user_data["activity"] = update.message.text
    await update.message.reply_text(CITY_TEXT)
    context.user_data["current_state"] = CITY
    return CITY


async def city_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await activity_handler(update, context)
    context.user_data["city"] = update.message.text
    await update.message.reply_text(CALORIES_TEXT)
    context.user_data["current_state"] = CALORIES
    return CALORIES


async def calories_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return await city_handler(update, context)
    context.user_data["calories"] = update.message.text

    user = UserService().create_user(
        username=context.user_data["username"],
        weight=context.user_data["weight"],
        height=context.user_data["height"],
        age=context.user_data["age"],
        activity=context.user_data["activity"],
        city=context.user_data["city"],
        calories=context.user_data["calories"]
    )

    if user is None:
        await update.message.reply_text(PROFILE_ERROR)
        return CALORIES

    await update.message.reply_text(PROFILE_UPDATED)
    return ConversationHandler.END
