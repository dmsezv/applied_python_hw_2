from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from strings import WELCOME_TEXT
from services.user_service import UserService
from components.buttons import MAIN_MENU_BUTTONS, CREATE_PROFILE_BUTTON


async def start_handler(update: Update, context: CallbackContext):
    context.user_data.clear()
    user = UserService().get_user(update.message.from_user.username)
    reply_markup = ReplyKeyboardMarkup(MAIN_MENU_BUTTONS if user else CREATE_PROFILE_BUTTON, one_time_keyboard=True)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)
    return ConversationHandler.END
