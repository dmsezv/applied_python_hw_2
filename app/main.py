from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters

from config import BOT_TOKEN
from handlers.handlers import (
    start_handler, set_profile_start, weight_handler, height_handler, age_handler,
    activity_handler, city_handler, calories_handler, cancel, back_handler
)
from states import WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    set_profile_handler = ConversationHandler(
        entry_points=[CommandHandler("set_profile", set_profile_start)],
        states={
            WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, weight_handler)],
            HEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, height_handler)],
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age_handler)],
            ACTIVITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, activity_handler)],
            CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, city_handler)],
            CALORIES: [MessageHandler(filters.TEXT & ~filters.COMMAND, calories_handler)]
        },
        fallbacks=[CommandHandler("cancel", cancel), CommandHandler("back", back_handler)],
    )

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(set_profile_handler)

    app.run_polling()
