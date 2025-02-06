from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    WELCOME_TEXT, CANCEL_MESSAGE, BACK_NOT_POSSIBLE, START_BUTTON
)


async def back_handler(update: Update, context: CallbackContext) -> int:
    current_state = context.user_data.get("current_state")
    if current_state is not None:
        return current_state
    await update.message.reply_text(BACK_NOT_POSSIBLE)
    return ConversationHandler.END


async def cancel_handler(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(CANCEL_MESSAGE)
    return ConversationHandler.END


async def start_handler(update: Update, context: CallbackContext):
    context.user_data.clear()
    reply_markup = ReplyKeyboardMarkup([[START_BUTTON]], one_time_keyboard=True)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)
    return ConversationHandler.END


async def view_profile_handler(update: Update, context: CallbackContext):
    # Здесь будет логика для отображения профиля пользователя
    await update.message.reply_text("Ваш профиль: ...")


async def delete_profile_handler(update: Update, context: CallbackContext):
    # Здесь будет логика для удаления профиля пользователя
    await update.message.reply_text("Ваш профиль удален.")
