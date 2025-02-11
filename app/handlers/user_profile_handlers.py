from telegram import Update
from telegram.ext import CallbackContext, ConversationHandler
from services.user_service import UserService
from strings import PROFILE_NOT_FOUND, PROFILE_VIEW, PROFILE_DELETED, PROFILE_DELETE_ERROR

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
                calories=user.calories,
                gender=user.gender
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
