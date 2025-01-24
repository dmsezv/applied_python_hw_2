from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from states import WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES
from strings import (
    WELCOME_TEXT, WEIGHT_TEXT, HEIGHT_TEXT, AGE_TEXT, ACTIVITY_TEXT,
    CITY_TEXT, CALORIES_TEXT, PROFILE_UPDATED, CANCEL_MESSAGE, BACK_NOT_POSSIBLE,
    LOG_WATER_SUCCESS, LOG_WATER_ERROR, LOG_FOOD_PROMPT, LOG_FOOD_ERROR,
    LOG_WORKOUT_SUCCESS, LOG_WORKOUT_ERROR, CHECK_PROGRESS
)


def back_handler(update: Update, context: CallbackContext) -> int:
    current_state = context.user_data.get("current_state")
    if current_state is not None:
        return current_state
    update.message.reply_text(BACK_NOT_POSSIBLE)
    return ConversationHandler.END


def set_profile_start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(WEIGHT_TEXT)
    context.user_data["current_state"] = WEIGHT
    return WEIGHT


def weight_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return set_profile_start(update, context)
    context.user_data["weight"] = update.message.text
    update.message.reply_text(HEIGHT_TEXT)
    context.user_data["current_state"] = HEIGHT
    return HEIGHT


def height_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return weight_handler(update, context)
    context.user_data["height"] = update.message.text
    update.message.reply_text(AGE_TEXT)
    context.user_data["current_state"] = AGE
    return AGE


def age_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return height_handler(update, context)
    context.user_data["age"] = update.message.text
    update.message.reply_text(ACTIVITY_TEXT)
    context.user_data["current_state"] = ACTIVITY
    return ACTIVITY


def activity_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return age_handler(update, context)
    context.user_data["activity"] = update.message.text
    update.message.reply_text(CITY_TEXT)
    context.user_data["current_state"] = CITY
    return CITY


def city_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return activity_handler(update, context)
    context.user_data["city"] = update.message.text
    update.message.reply_text(CALORIES_TEXT)
    context.user_data["current_state"] = CALORIES
    return CALORIES


def calories_handler(update: Update, context: CallbackContext) -> int:
    if update.message.text == "/back":
        return city_handler(update, context)
    context.user_data["calories"] = update.message.text
    update.message.reply_text(PROFILE_UPDATED)
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(CANCEL_MESSAGE)
    return ConversationHandler.END


def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text(WELCOME_TEXT)
