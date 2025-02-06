from telegram.ext import (
    ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters, CallbackQueryHandler
)
from config import BOT_TOKEN

from handlers.set_profile_handlers import (
    set_profile_start, weight_handler, height_handler, age_handler,
    activity_handler, city_handler, calories_handler, gender_handler
)
from handlers.set_profile_handlers import WEIGHT, HEIGHT, AGE, ACTIVITY, CITY, CALORIES, GENDER
from handlers.common_handlers import back_handler, cancel_handler, start_handler, view_profile_handler, delete_profile_handler
from strings import START_BUTTON


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    set_profile_handler = ConversationHandler(
        entry_points=[
            CommandHandler("set_profile", set_profile_start),
            MessageHandler(filters.Regex(f"^{START_BUTTON}$"), set_profile_start)
        ],
        states={
            WEIGHT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, weight_handler),
            ],
            HEIGHT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, height_handler),
            ],
            AGE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, age_handler),
            ],
            ACTIVITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, activity_handler),
            ],
            CITY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, city_handler),
            ],
            CALORIES: [
                CallbackQueryHandler(calories_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, calories_handler),
            ],
            GENDER: [
                CallbackQueryHandler(gender_handler),
                MessageHandler(filters.TEXT & ~filters.COMMAND, gender_handler),
            ]
        },
        fallbacks=[
            CommandHandler("start", start_handler),
            CommandHandler("cancel", cancel_handler),
            CommandHandler("back", back_handler)
        ],
        allow_reentry=True
    )

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(set_profile_handler)
    app.add_handler(CallbackQueryHandler(view_profile_handler, pattern='^view_profile$'))
    app.add_handler(CallbackQueryHandler(delete_profile_handler, pattern='^delete_profile$'))
    app.run_polling()


if __name__ == "__main__":
    main()
