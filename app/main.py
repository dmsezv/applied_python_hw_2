from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters,
    CallbackQueryHandler, CallbackContext
)
from telegram import Update

from config import BOT_TOKEN

from handlers.set_profile_handlers import (
    set_profile_start, weight_handler, height_handler, age_handler,
    activity_handler, city_handler, calories_handler
)
from handlers.set_profile_handlers import WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES
from handlers.common_handlers import start_handler, back_handler, cancel_handler


async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'set_profile':
        await set_profile_start(update, context)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    set_profile_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button_handler)],
        states={
            WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, weight_handler)],
            HEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, height_handler)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age_handler)],
            ACTIVITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, activity_handler)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, city_handler)],
            CALORIES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calories_handler)]
        },
        fallbacks=[CommandHandler("cancel", cancel_handler), CommandHandler("back", back_handler)],
    )

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(set_profile_handler)

    app.run_polling()