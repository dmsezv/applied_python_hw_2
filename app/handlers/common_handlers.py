from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import (
    WELCOME_TEXT, CANCEL_MESSAGE, BACK_NOT_POSSIBLE,
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
    keyboard = [[InlineKeyboardButton("Создать профиль", callback_data='set_profile')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)
